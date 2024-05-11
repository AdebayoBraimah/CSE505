Batch Downloading Course Data
===============================

In the case of the ``CSE`` major -- there are many courses that are required as either degree requirements or as prerequisites for other courses.  
It is recommnended to download all possible course prerequisites and requirements. However, doing so is a highly time consuming process.
The batch scripts located in ``src/scripts`` can be used to download all of the course data for a given major. 
However, the wrapper script ``src/scripts/download_courses.sh`` contains an additional external dependency: `GNU parallel<https://www.gnu.org/software/parallel/>`_.
Once GNU parallel has been installed, the script can be run as follows:

.. code-block:: bash

    cd src/scripts
    ./download_courses.sh

Additionally, the number of jobs that can be run in parallel can be specified by editing the integer next to the ``-j`` flag in the script.

.. note::

    - All of the course data is stored in the ``resources`` sub-directory of ``src``.

Below is the bash script that is used to batch download all the correspoding course data:

.. code-block:: bash

    #!/usr/bin/env bash

    download_courses=$(realpath download_courses.py)

    # Array of course majors
    courses=(
        "cse"
        "ams"
        "bio"
        "phy"
        "ast"
        "mat"
        "che"
        "geo"
        "ise"
        "wrt"
        "bme"
        "esg"
        "ese"
        "mec"
        "psy"
    )

    # Create job file
    job_file="job.txt"

    # Remove job file if it exists
    if [[ -f ${job_file} ]]; then
        rm ${job_file}
    fi

    # Loop through each course major
    for course in "${courses[@]}"; do
        # ${download_courses} ${course}
        echo "${download_courses} ${course}" >> ${job_file}
    done

    # Run job file
    parallel -j 4 < ${job_file} # Change the integer to the number of jobs to run in parallel


Additionally, this is the python script that is used to download the course data:

.. code-block:: python

    #!/usr/bin/env python3
    """Download course data from Stony Brook University's Solar course catalog.
    """

    import os
    import sys

    _PKG_PATH = "/Users/adebayobraimah/Desktop/projects/CSE505"

    sys.path.append(_PKG_PATH)

    from src import RESROURCEDIR
    from src.kg.knowledge_graph import scrape_sbu_solar, KnowledgeGraph
    from src.ergoai.ergoai import json_to_ergo
    from src.clapi.clapi import process_course_data_clingo

    url: str = (
        "https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?"
    )


    def main(major: str) -> None:
        outname: str = os.path.join(RESROURCEDIR, f"{major}")

        if not (os.path.exists(f"{outname}_courses.json")):
            kg = scrape_sbu_solar(
                url,
                major_three_letter_code=major,
                wait_time=10,
                headless=True,
                verbose=True,
            )
            kg.df.to_csv(f"{outname}_courses.csv", index=True)
            kg.df.to_json(f"{outname}_courses.json", orient="index", indent=4)

        if not (os.path.exists(f"{outname}_courses.lp")):
            process_course_data_clingo(
                json_file=f"{outname}_courses.json",
                output_file=f"{outname}_courses.lp",
                repeatable_courses=[("cse593", "_", "_")],
            )

        if not (os.path.exists(f"{outname}_courses.ergo")):
            json_to_ergo(json_file=f"{outname}_courses.json")

        return None


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: download_courses.py <major>")
            sys.exit(1)

        main(sys.argv[1])

Downloading the course data in parallel in this fashion saves a significant amount of time.

.. note::

    - The output directory can be modified, simply replace ``RESROURCEDIR`` with the desired directory path.
