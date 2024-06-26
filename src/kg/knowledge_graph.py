"""Knowledge graph module for this project.

.. autosummary::
    :nosignatures:

    KnowledgeBaseError
    KnowledgeGraphError
    KnowledgeBase
    KnowledgeGraph
    scrape_sbu_solar
    parse_requirements
    parse_prerequisites
    clean_course_title
    remove_non_numeric
    get_course_components
    get_sbu_cse_undergrad_course_offered_info
    get_sbu_cse_grad_course_offered_info
    get_sbu_cse_course_offered_info
"""

import os
import re
import time
import pandas as pd
import requests

from bs4 import BeautifulSoup
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from typing import Any, Optional, List, Tuple, Union
from warnings import warn

from src.utils import util
from src.utils.util import timeit


class KnowledgeBaseError(Exception):
    """Exception intended for knowledge base errors."""

    pass


class KnowledgeGraphError(Exception):
    """Exception intended for knowledge graph errors."""

    pass


@dataclass
class KnowledgeGraph:
    """Dataclass intended to encapsulate knowledge graphs.

    NOTE:
        - Only one knowledge graph file needs to be specified.

    Example usage:
        >>> kg = KnowledgeGraph(json="path/to/file.json")
        >>> kg.json
        'path/to/file.json'

    Raises:
        KnowledgeGraphError: Arises if the knowledge graph file is not specified. Valid knowledge graph files include JSON, ERGO, RDF, OWL, CSV files.

    Attributes:
        json: JSON knowledge graph file.
        ergo: ERGO knowledge graph file.
        rdf: RDF knowledge graph file.
        owl: OWL knowledge graph file.
        csv: CSV knowledge graph file.
        lp: Logic programming (``Clingo``) knowledge graph file.
    """

    json: str = ""
    ergo: str = ""
    rdf: str = ""
    owl: str = ""
    csv: str = ""
    df: pd.DataFrame = pd.DataFrame()
    lp: str = ""

    def __post_init__(self):
        """Post-initialization function to verify knowledge graph file or representation.

        Raises:
            ValueError: Arises if the knowledge graph file or representation is not specified. Valid knowledge graph files include JSON, ERGO, RDF, OWL, CSV files, and a valid representation includes a ``pandas data frame``.
            FileNotFoundError: Arises if the file does not exist.
        """
        self.json: str = (
            os.path.abspath(self.json)
            if (self.json and self.json.lower().endswith(".json"))
            else None
        )
        self.ergo: str = (
            os.path.abspath(self.ergo)
            if (self.ergo and self.ergo.lower().endswith(".ergo"))
            else None
        )
        self.rdf: str = (
            os.path.abspath(self.rdf)
            if (self.rdf and self.rdf.lower().endswith(".rdf"))
            else None
        )
        self.owl: str = (
            os.path.abspath(self.owl)
            if (self.owl and self.owl.lower().endswith(".owl"))
            else None
        )

        self.csv: str = (
            os.path.abspath(self.csv)
            if (self.csv and self.csv.lower().endswith(".csv"))
            else None
        )

        self.df: pd.DataFrame = self.df if (len(self.df) != 0) else None

        self.lp: str = (
            os.path.abspath(self.lp)
            if (self.lp and self.lp.lower().endswith(".lp"))
            else None
        )

        # Check if knowledge graph file or representation is specified
        if (
            (not self.json)
            and (not self.ergo)
            and (not self.rdf)
            and (not self.owl)
            and (not self.csv)
            and (not self.lp)
            and (len(self.df) == 0)
        ):
            raise KnowledgeGraphError(
                "Knowledge graph file or representation must be specified."
            )

        # Check if file exists
        for file in [self.json, self.ergo, self.rdf, self.owl, self.csv, self.lp]:
            if file and (not os.path.exists(file)):
                raise FileNotFoundError(f"File not found: {file}")


@dataclass
class KnowledgeBase:
    """Dataclass intended to encapsulate knowledge bases.

    NOTE:
        - Only one knowledge base file needs to be specified.

    Example usage:
        >>> kb = KnowledgeBase(url="https://www.stonybrook.edu")
        >>> kb.url
        'https://www.stonybrook.edu'

    Raises:
        KnowledgeBaseError: Arises if the knowledge base file or representation is not specified. Valid knowledge base files include PDF, TXT or ERGO files, and valid representations include a URL.

    Attributes:
        url: URL knowledge base website link.
        pdf: PDF knowledge base file.
        txt: TXT knowledge base file.
        ergo: ERGO knowledge base file.
        lp: Logic programming (``Clingo``) knowledge base file.
    """

    url: str = ""
    pdf: str = ""
    txt: str = ""
    ergo: str = ""
    lp: str = ""

    def __post_init__(self):
        """Post-initialization function to verify knowledge base file or representation.

        Raises:
            KnowledgeBaseError: Arises if the knowledge base file or representation is not specified. Valid knowledge base files include PDF, TXT files.
            FileNotFoundError: Arises if the file does not exist.
        """
        self.pdf: str = (
            os.path.abspath(self.pdf)
            if (self.pdf and self.pdf.lower().endswith(".pdf"))
            else None
        )
        self.txt: str = (
            os.path.abspath(self.txt)
            if (self.txt and self.txt.lower().endswith(".txt"))
            else None
        )

        self.ergo: str = (
            (os.path.abspath(self.ergo))
            if (self.ergo and self.ergo.lower().endswith(".ergo"))
            else None
        )

        self.lp: str = (
            (os.path.abspath(self.lp))
            if (self.lp and self.lp.lower().endswith(".lp"))
            else None
        )

        # Check if knowledge base file or representation is specified
        if (
            (not self.url)
            and (not self.pdf)
            and (not self.txt)
            and (not self.ergo)
            and (not self.lp)
        ):
            raise KnowledgeBaseError(
                "Knowledge base file or representation must be specified."
            )

        # Check if file exists
        for file in [self.pdf, self.txt, self.ergo]:
            if file and (not os.path.exists(file)):
                raise FileNotFoundError(f"File not found: {file}")


@timeit
def scrape_sbu_solar(
    url: Union[KnowledgeBase, str],
    major_three_letter_code: str,
    wait_time: int = 10,
    headless: bool = True,
    verbose: bool = False,
    output_filename: Optional[str] = None,
) -> KnowledgeGraph:
    """Scrape Stony Brook University's course catalog for a specific major's course information.
    This function scrapes Stony Brook University's course catalog and stores the information in a :class:`KnowledgeGraph` object.
    The course information includes course number, title, career, units, grading basis, enrollment requirements, anti-requisites, corequisites, course components, academic group, academic organization, and course description.
    Additionally, information to when courses are offered over a 4 semester span (specific only to CSE courses) is also included. This information is scraped from the CSE department's website, and is
    hardcoded for CSE courses only see (:func:`get_sbu_cse_course_offered_info`).

    WARNING:
        - This function uses a ``Selenium WebDriver`` and specific ``div`` IDs to scrape the course catalog.

    Usage example:
        >>> url = "https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?"
        >>> kg = scrape_sbu_solar(
        ...        url=url,
        ...        major_three_letter_code="cse",
        ...        wait_time=10,
        ...        headless=True,
        ...        verbose=True,)

    Args:
        url: Input Stony Brook URL (or :class:`KnowledgeBase` object) to scrape.
        major_three_letter_code: Three letter code for the major (e.g. CSE for computer science).
        wait_time: Maximum wait time (in seconds) for each click operation. Defaults to 10.
        headless: Do not open brower. Defaults to True.
        verbose: Print output to screen. Defaults to False.
        output_filename: Output filename for the JSON file. Defaults to None.

    Raises:
        ValueError: Arises if the course table is not displayed, is empty, or if the wait time is less than 0 seconds.

    Returns:
        :class:`KnowledgeGraph` object containing course information that corresponds to an output JSON file.
    """

    # Verify output_filename
    if output_filename is not None:
        _path, _filename, _ = util.file_parts(output_filename)
        output_filename: str = os.path.join(
            _path, f"{_filename}.json"
        )  # Ensure JSON extension
        _return_json: bool = True
    else:
        _return_json: bool = False

    # Verify URL
    if isinstance(url, KnowledgeBase):
        url: str = url.url

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

    # NOTE: If major code is 'MAT', then partial
    #  link text is 'MAT - M' must be used to navigate
    #
    # Navigate to major
    if major_three_letter_code == "MAT":
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, f"{major_three_letter_code} - M")
            )
        ).click()
    else:
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
        # return None
        raise ValueError("Table is not displayed. Check the URL and major code.")

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

    # Clean course titles
    _course_titles: List[str] = df["Course Title"].tolist()
    df["Course Title"] = [clean_course_title(title) for title in _course_titles]

    career_list: List[str] = []
    units_list: List[str] = []
    grading_basis_list: List[str] = []
    enrollment_requirement_list: List[str] = []
    enrollment_anti_requisite_list: List[str] = []
    enrollment_corequisite_list: List[str] = []
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
            units: str = float(
                driver.find_element(By.ID, "DERIVED_CRSECAT_UNITS_RANGE$0").text
            )
        except (ValueError, NoSuchElementException):
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

        # Enrollment requirements (prerequisites, anti-requisites, and corequisites)
        try:
            _enrollment_requirement: str = driver.find_element(
                By.ID, "DERIVED_CRSECAT_DESCR254A$0"
            ).text
        except NoSuchElementException:
            _enrollment_requirement: str = ""

        enrollment_requirement: Union[str, List[List[str]]]
        enrollment_anti_requisite: Union[str, List[List[str]]]
        enrollment_corequisite: Union[str, List[List[str]]]

        enrollment_requirement, enrollment_anti_requisite, enrollment_corequisite = (
            parse_requirements(input_string=_enrollment_requirement)
        )

        # Course components
        course_components: Tuple[str, ...] = get_course_components(driver)

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

        # Append course number with three letter code
        course = remove_non_numeric(course)
        course_numbers_with_three_letter_code.append(
            f"{major_three_letter_code}{course}"  # Remove space character, output should be: "CSE101"
        )

        # Update lists
        career_list.append(career)
        units_list.append(units)
        grading_basis_list.append(grading_basis)
        enrollment_requirement_list.append(enrollment_requirement)
        enrollment_anti_requisite_list.append(enrollment_anti_requisite)
        enrollment_corequisite_list.append(enrollment_corequisite)
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
    df.insert(df.columns.__len__(), "Antirequisites", enrollment_anti_requisite_list)
    df.insert(df.columns.__len__(), "Corequisites", enrollment_corequisite_list)
    df.insert(df.columns.__len__(), "Course Components", course_components_list)
    df.insert(df.columns.__len__(), "Academic Group", academic_group_list)
    df.insert(df.columns.__len__(), "Academic Organization", academic_organization_list)
    df.insert(df.columns.__len__(), "Description", description_list)

    # Rename columns
    df.rename(
        columns={
            "Enrollment Requirement": "Prerequisites",
            "Units": "Credits",
            "Course Title": "CourseTitle",
            "Course Nbr": "CourseNumber",
        },
        inplace=True,
    )

    # Add semester offering information here
    if major_three_letter_code.upper() == "CSE":
        # Get course offering information for CSE
        _df = get_sbu_cse_course_offered_info(
            undergrad_url="https://www.cs.stonybrook.edu/students/Undergraduate-Studies/csecourses",  # Hard code as this is for CSE only
            grad_url="https://www.cs.stonybrook.edu/students/Graduate-Studies/courses",  # Hard code as this is for CSE only
        )

        # Get dataframe headers
        current_columns: List[str] = df.columns.tolist()
        _df_columns: List[str] = _df.columns.tolist()  # [
        #     -4:
        # ]  # Only need the last 4 columns, as that has the course semester offering information
        new_columns: List[str] = current_columns + _df_columns

        # Concatenate along CourseNumber (columns)
        df2 = pd.concat([df, _df], axis=1, ignore_index=True)
        df = df2.fillna(0)

        # Rename columns in the new DataFrame
        df.columns = new_columns

        # Remove duplicate columns
        df = df.loc[:, ~df.columns.duplicated()]

        # Update course offering information for certain CSE courses
        #
        # TODO: Keep adding courses that are regularly offered but
        #       not scheduled here.
        for rows in df.itertuples():
            if (
                ("593" in rows[1].lower())
                or ("600" in rows[1].lower())
                or ("698" in rows[1].lower())
                or ("487" in rows[1].lower())
            ):
                df.iloc[rows[0], -4:] = [1, 1, 1, 1]
    else:
        # Non-CSE cases -- just assume that courses are offered all year round
        new_columns: List[str] = ["spring1", "fall1", "spring2", "fall2"]
        for column in new_columns:
            df[column] = 1

    # Condense semester offering information to just one fall and spring column each
    df["spring"] = df[["spring1", "spring2"]].max(axis=1)
    df["fall"] = df[["fall1", "fall2"]].max(axis=1)

    # Replace index with Course Nbr
    df.set_index(
        # "Course Nbr",
        "CourseNumber",
        inplace=True,
        drop=True,  # Drop the Index column
    )

    # Remove duplicate rows
    df = df[~df.index.duplicated(keep="first")]

    # Drop columns not needed by ErgoAI
    df.drop(
        [
            # "Description",
            "Academic Group",
            "Academic Organization",
            "Course Components",
            "Grading Basis",
            "spring1",
            "fall1",
            "spring2",
            "fall2",
        ],
        axis=1,
        inplace=True,
    )

    # Quit the driver, close the browser
    driver.quit()

    # Write to JSON file if requested
    if _return_json:
        df.to_json(output_filename, orient="index", indent=4)

    # Create KnowledgeGraph object
    kg = KnowledgeGraph(df=df, json=output_filename)

    return kg


def parse_prerequisites(input_string: str) -> Union[str, List[List[str]]]:
    """Parse major requirements from a string into a list of lists of course codes.
    This function is mainly used to separate disjunctions and conjunctions course prerequisites.
    Disjunctions are grouped together in the same sub-list, while conjunctions are separated into different sub-lists.
    For example, ``"Prerequisite: CSE 216 or CSE 260; AMS 310; CSE major"`` would be parsed as: ``[["CSE 216", "CSE 260"], ["AMS 310"], ["CSE major"]]``.

    WARNING:
        - This function is deprecated. Use :py:func:`~src.kg.knowledge_graph.parse_requirements` instead.

    Usage example:
        >>> input_string = "Prerequisite: CSE 216 or CSE 260; AMS 310; CSE major"
        >>> parse_prerequisites(input_string)
        [['CSE 216', 'CSE 260'], ['AMS 310'], ['CSE major']]

    Args:
        input_string: Input string containing major course requirements.

    Returns:
        List of lists of containing strings that corresponds to course prequisites.
    """
    warn(
        "``parse_prerequisites()`` is deprecated. Please use ``parse_requirements()`` instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    # NOTE: Disjunction statements in the same sub-list,
    #   conjunctions in separate lists

    # NOTE: This pattern assumes that course codes are always in
    #   the format "AAA 123"
    # Define a regular expression pattern to capture course codes
    course_pattern = r"\b([A-Z]{3} \d{3})\b"

    # Split the input string into major requirements using the semi-colon
    conjunctive_parts = input_string.split(";")

    # Result list to hold parsed requirements
    result = []

    for part in conjunctive_parts:
        # Find courses in each part
        part_courses = re.findall(course_pattern, part)

        # Add non-empty lists to the result
        if part_courses:
            result.append(part_courses)

    if not result:
        return "NONE"

    return result


def parse_requirements(
    input_string: str,
) -> Tuple[List[List[str]], List[List[str]], List[List[str]]]:
    """Parse major requirements from a string into a list of lists of course codes.
    This function is mainly used to separate disjunctions and conjunctions of course: prerequisites,
    anti-requisites and corequisites. Disjunctions are grouped together in the same sub-list, while conjunctions
    are separated into different sub-lists. Returns lists for prerequisites, anti-requisites, and corequisites.

    NOTE:
        - Disjunctive statements will appear in the same sub-list, while conjunctive statements will appear in a separate sub-list.
        - Use this function in place of :py:func:`~src.kg.knowledge_graph.parse_prerequisites`.

    Usage example:
        >>> input_string = "Prerequisite: CSE 216 or CSE 260; AMS 310; Anti-requisite: CSE 260. Corequisite: CSE 161."
        >>> parse_requirements(input_string)
        ([['CSE216', 'CSE260'], ['AMS310']], [['CSE260']], [['CSE161']])

    Args:
        input_string: Input string containing major course requirements.

    Returns:
        Tuple of lists containing strings that corresponds to course prerequisites, anti-requisites, and corequisites.
    """
    # Normalize spaces and split the string into main sections
    input_string = re.sub(r"\s+", " ", input_string.strip())

    if "co-requisite" in input_string.lower():
        input_string = input_string.replace("co-requisite", "corequisite:")

    # Find each type of requirement by searching for specific keywords
    prereq_match = re.search(
        r"Prerequisites?: (.*?)(?=(Anti-requisite|Corequisite|$))",
        input_string,
        re.IGNORECASE,
    )
    antireq_match = re.search(
        r"Anti-requisite: (.*?)(?=(Prerequisite|Corequisite|$))",
        input_string,
        re.IGNORECASE,
    )
    coreq_match = re.search(
        r"Corequisite: (.*?)(?=(Prerequisite|Anti-requisite|$))",
        input_string,
        re.IGNORECASE,
    )

    def extract_courses(section):
        if not section:
            return []
        # Split sections into parts based on semicolon or "and" as conjunctions
        parts = re.split(r";| and ", section)
        # For each part, find disjunctions or standalone courses and remove spaces
        courses = [
            re.findall(r"[A-Z]{2,4}\d{3,4}", part.replace(" ", "")) for part in parts
        ]
        # Filter out empty lists
        return [course for course in courses if course]

    # TODO: Remove prerequisite if it contains 'MAP'
    prerequisites = extract_courses(prereq_match.group(1) if prereq_match else "")
    anti_requisites = extract_courses(antireq_match.group(1) if antireq_match else "")
    corequisites = extract_courses(coreq_match.group(1) if coreq_match else "")

    if not prerequisites:
        prerequisites = "NONE"

    if not anti_requisites:
        anti_requisites = "NONE"

    if not corequisites:
        corequisites = "NONE"

    return (prerequisites, anti_requisites, corequisites)


def get_course_components(driver: "webdriver") -> Tuple[str, ...]:
    """Helper function to get course components. Course components may include more than one word.

    Args:
        driver: (``Selenium WebDriver``) Input webdriver object.

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


def clean_course_title(course_title: str) -> str:
    """Clean course title by removing any additional information after '**'.

    Args:
        course_title: Course title string.

    Returns:
        Cleaned course title string.
    """
    # Use a regular expression to match only the course title before '**'
    cleaned_title = re.sub(r"\*\*.*$", "", course_title).strip()
    return cleaned_title


def remove_non_numeric(course_number: str) -> str:
    """Remove any non-digit characters from the course number.

    Args:
        course_number: Course number string.

    Returns:
        Cleaned course number string.
    """
    # Remove any non-digit characters from the string
    cleaned_number = re.sub(r"\D", "", course_number)
    return cleaned_number


def get_sbu_cse_undergrad_course_offered_info(url: str) -> pd.DataFrame:
    """Scrape Stony Brook University's undergraduate CSE course offering webpage.

    Usage example:
        >>> url = "https://www.cs.stonybrook.edu/students/Undergraduate-Studies/csecourses"
        >>> df = get_sbu_cse_undergrad_course_offered_info(url=url)

    Args:
        url: URL of the Stony Brook University undergraduate course offering webpage.

    Returns:
        Pandas DataFrame containing the undergraduate course offering information.
    """
    # Get the HTML content of the page
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing the course information
    table = soup.find("table", class_="views-table views-view-table cols-7")

    # Get the headers of the table
    headers: List[Any] = [header.text.strip() for header in table.find_all("th")]

    # Get table rows
    rows: List[Any] = []

    # Iterate over each row in the table, skip the header row
    for row in table.find_all("tr")[1:]:
        columns: List[Any] = []
        for idx, col in enumerate(row.find_all("td")):
            text = col.text.strip()
            # Check if the header for this column is a semester column
            if any(term in headers[idx] for term in ["Spring", "Summer", "Fall"]):
                # Process for presence of '✔'
                if "✔" in text:
                    columns.append(1)
                else:
                    columns.append(0)
            else:
                # Keep original text for non-semester columns
                columns.append(text)
        rows.append(columns)

    df = pd.DataFrame(rows, columns=headers)
    return df


def get_sbu_cse_grad_course_offered_info(url: str) -> pd.DataFrame:
    """Scrape Stony Brook University's CSE graduate course offering webpage.

    Usage example:
        >>> url = "https://www.cs.stonybrook.edu/students/Graduate-Studies/courses"
        >>> df = get_sbu_cse_grad_course_offered_info(url=url)

    Args:
        url: URL of the Stony Brook University graduate course offering webpage.

    Returns:
        Pandas DataFrame containing the graduate course offering information.
    """
    # Get the HTML content of the page
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing the course information
    table = soup.find("table", class_="views-table views-view-table cols-6")

    # Get the headers of the table
    headers: List[Any] = [header.text.strip() for header in table.find_all("th")]

    # Get table rows
    rows: List[Any] = []

    # Iterate over each row in the table, skip the header row
    for row in table.find_all("tr")[1:]:
        columns: List[Any] = []
        for idx, col in enumerate(row.find_all("td")):
            text = col.text.strip()
            # Check if the header for this column is a semester column
            if any(term in headers[idx] for term in ["Spring", "Summer", "Fall"]):
                # Process for presence of '✔'
                if "✔" in text:
                    columns.append(1)
                else:
                    columns.append(0)
            else:
                # Keep original text for non-semester columns
                columns.append(text)
        rows.append(columns)

    df = pd.DataFrame(rows, columns=headers)
    return df


def get_sbu_cse_course_offered_info(undergrad_url: str, grad_url: str) -> pd.DataFrame:
    """Scrape Stony Brook University's CSE undergraduate and graduate course offering webpages.

    WARNING:
        - The URLs used in ``Usage example`` were (accessed and) current as of May 03 2024.
        - The tables located at each URL contain information: Spring 2023, Fall 2023, Spring 2024, and Fall 2024 -- this will need to be updated in this function in the future.

    Usage example:
        >>> undergrad_url = "https://www.cs.stonybrook.edu/students/Undergraduate-Studies/csecourses"
        >>> grad_url = "https://www.cs.stonybrook.edu/students/Graduate-Studies/courses"
        >>> df = get_sbu_cse_course_offered_info(undergrad_url=undergrad_url, grad_url=grad_url)

    Args:
        undergrad_url: URL of the Stony Brook University undergraduate course offering webpage.
        grad_url: URL of the Stony Brook University graduate course offering webpage.

    Returns:
        Pandas DataFrame containing the undergraduate and graduate course offering information.
    """
    # Scrape undergraduate course information
    df1 = get_sbu_cse_undergrad_course_offered_info(url=undergrad_url)

    # Scrape graduate course information
    df2 = get_sbu_cse_grad_course_offered_info(url=grad_url)

    # Combine both dataframes
    df = pd.concat([df1, df2], axis=0, ignore_index=True).drop(["Summer 2024"], axis=1)

    # Rename columns
    df.rename(
        columns={
            "Course Name": "CourseNumber",
            "Course Title": "CourseTitle",
            "Spring 2023": "spring1",
            "Fall 2023": "fall1",
            "Spring 2024": "spring2",
            "Fall 2024": "fall2",
        },
        inplace=True,
    )
    return df
