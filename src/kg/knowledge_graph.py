"""Knowledge graph module for this project.

.. autosummary::
    :nosignatures:

    create_knowledge_graph
    scrape_sbu_solar

.. autoclass:: KnowledgeGraph
    :members:

.. autoclass:: KnowledgeBase
    :members:
"""

import os
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from typing import Optional, List, Tuple, Union

from src.utils.util import file_parts


class KnowledgeGraph:
    pass


class KnowledgeBase:
    pass


def create_knowledge_graph():
    pass


def scrape_sbu_solar(
    url: str,
    major_three_letter_code: str,
    wait_time: int = 10,
    headless: bool = True,
    verbose: bool = False,
    output_filename: Optional[str] = None,
) -> Union[pd.DataFrame, str]:
    """Scrape Stony Brook University's course catalog for a specific major's course information.

    Usage example:
        >>> df = scrape_sbu_solar(
        ...        url=url,
        ...        major_three_letter_code="cse",
        ...        wait_time=10,
        ...        headless=True,
        ...        verbose=True,)

    Args:
        url: Input Stony Brook URL to scrape.
        major_three_letter_code: Three letter code for the major (e.g. CSE for computer science).
        wait_time: Maximum wait time for each click operation. Defaults to 10.
        headless: Do not open brower. Defaults to True.
        verbose: Print output to screen. Defaults to False.
        output_filename: Output filename for the JSON file. If specified, this filename is returned (in addition to a JSON file being created). If not specified, a Pandas ``dataframe`` is returned instead. Defaults to None.

    Raises:
        ValueError:
            * Arises if the course table is not displayed.
            * Arises if the course table is empty.
            * Arises if the wait time is less than 0 seconds.

    Returns:
        Either a Pandas ``dataframe`` or a JSON file (if ``output_filename`` is specified).
    """

    # Verify output_filename
    if output_filename is not None:
        _path, _filename, _ = file_parts(output_filename)
        output_filename: str = os.path.join(
            _path, f"{_filename}.json"
        )  # Ensure JSON extension
        _return_json: bool = True
    else:
        _return_json: bool = False

    # Verify wait time is integer and greater than 0
    wait_time: int = int(wait_time)

    # Headless option
    if headless:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
    else:
        options = None

    if wait_time < 0:
        raise ValueError("Wait time must be greater than 0 seconds.")

    # Setup Selenium WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Get page navigation letter
    major_three_letter_code: str = (
        major_three_letter_code.upper()
    )  # Ensure major code is uppercase

    nav_letter: str = major_three_letter_code[
        0
    ].upper()  # Get first letter of major code

    # NOTE: If Major ID starts with 'A', skip this step.
    #
    # Click on the letter to navigate to the major
    if nav_letter == "A":
        pass
    else:
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nav_letter))
        ).click()

    # Navigate to major
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, major_three_letter_code))
    ).click()

    # Get table data
    time.sleep(wait_time // 2)  # Time to wait for javascript to load the table.
    table: List[webdriver.remote.webelement.WebElement] = driver.find_elements(
        By.TAG_NAME, "tbody"
    )  # This will be a list of tables

    # Remove tables without course number
    # Perform this in reverse order to avoid index errors
    #   if table is removed from the list
    for tab in reversed(table):
        try:
            tab.find_element(By.PARTIAL_LINK_TEXT, "Course Nbr")
        except (AttributeError, NoSuchElementException):
            table.remove(tab)

    try:
        table = table[-1]  # Get the last table
    except IndexError:
        return None

    # Verify table
    if not table.is_displayed():
        raise ValueError("Table is not displayed. Check the URL and major code.")

    if not table.text:
        raise ValueError("Table is empty. Check the URL and major code.")

    # Extract headers
    headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]

    # Extract rows
    rows = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        cells = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if cells:  # This check is to skip rows without table data cells
            rows.append(cells)

    # Create DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Create additional columns for course information
    _course_numbers: List[str] = df["Course Nbr"].tolist()  # Get course numbers

    career_list: List[str] = []
    units_list: List[str] = []
    grading_basis_list: List[str] = []
    enrollment_requirement_list: List[str] = []
    course_components_list: List[Tuple[str, ...]] = []
    academic_group_list: List[str] = []
    academic_organization_list: List[str] = []
    description_list: List[str] = []
    course_numbers_with_three_letter_code: List[str] = []

    if verbose:
        print(f"\nScraping course information for {major_three_letter_code}...\n")

    # Get information for each course
    for course in _course_numbers:

        if verbose:
            print(f"Processing course: {course}...")

        # Wait for the page to load and click on course number
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.LINK_TEXT, f"{course}"))
        ).click()

        # Use ID to find element -- it is unique.
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located(
                (By.ID, "win0divSSR_CRSE_OFF_VW_ACAD_CAREER$0")
            )
        ).click()

        try:
            career: str = driver.find_element(
                By.ID, "win0divSSR_CRSE_OFF_VW_ACAD_CAREER$0"
            ).text
        except NoSuchElementException:
            career: str = ""

        # Course units
        try:
            units: str = driver.find_element(
                By.ID, "DERIVED_CRSECAT_UNITS_RANGE$0"
            ).text
        except NoSuchElementException:
            units: str = ""

        # Grading basis
        try:
            grading_basis: str = driver.find_element(
                By.ID, "win0divSSR_CRSE_OFF_VW_GRADING_BASIS$0"
            ).text
        except NoSuchElementException:
            grading_basis: str = ""

        # Enrollment requirements (pre-requisites)
        try:
            enrollment_requirement: str = driver.find_element(
                By.ID, "DERIVED_CRSECAT_DESCR254A$0"
            ).text
        except NoSuchElementException:
            enrollment_requirement: str = ""

        # Course components
        course_components: Tuple[str, ...] = _get_course_components(driver)

        # Academic group
        try:
            academic_group: str = driver.find_element(
                By.ID, "ACAD_GROUP_TBL_DESCR$0"
            ).text
        except NoSuchElementException:
            academic_group: str = ""

        # Academic organization
        try:
            academic_organization: str = driver.find_element(
                By.ID, "win0divACAD_ORG_TBL_DESCR$0"
            ).text
        except NoSuchElementException:
            academic_organization: str = ""

        # Course description
        try:
            description: str = driver.find_element(
                By.ID, "SSR_CRSE_OFF_VW_DESCRLONG$0"
            ).text
        except NoSuchElementException:
            description: str = ""

        # Update course number with three letter code
        course_numbers_with_three_letter_code.append(
            f"{major_three_letter_code} {course}"
        )

        # Update lists
        career_list.append(career)
        units_list.append(units)
        grading_basis_list.append(grading_basis)
        enrollment_requirement_list.append(enrollment_requirement)
        course_components_list.append(course_components)
        academic_group_list.append(academic_group)
        academic_organization_list.append(academic_organization)
        description_list.append(description)

        # Wait then click to go back to the course list
        WebDriverWait(driver, wait_time // 2).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Return to Browse Course Catalog")
            )
        ).click()

    # Update DataFrame
    df["Course Nbr"] = course_numbers_with_three_letter_code
    df.insert(df.columns.__len__(), "Career", career_list)
    df.insert(df.columns.__len__(), "Units", units_list)
    df.insert(df.columns.__len__(), "Grading Basis", grading_basis_list)
    df.insert(
        df.columns.__len__(), "Enrollment Requirement", enrollment_requirement_list
    )
    df.insert(df.columns.__len__(), "Course Components", course_components_list)
    df.insert(df.columns.__len__(), "Academic Group", academic_group_list)
    df.insert(df.columns.__len__(), "Academic Organization", academic_organization_list)
    df.insert(df.columns.__len__(), "Description", description_list)

    # Quit the driver, close the browser
    driver.quit()

    if _return_json:
        return df.to_json(output_filename, orient="records", indent=4)
    else:
        return df


def _get_course_components(driver: webdriver) -> Tuple[str, ...]:
    """Helper function to get course components. Course components may include more than one word.

    Args:
        driver: Selenium WebDriver object.

    Returns:
        Tuple that consists of course components.
    """
    course_components_list: List = []
    for num in range(0, 10):
        try:
            course_components_list.append(
                driver.find_element(By.ID, f"DERIVED_CRSECAT_DESCR${num}").text
            )
        except NoSuchElementException:
            return tuple(course_components_list)
