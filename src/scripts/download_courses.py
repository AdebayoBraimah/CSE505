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
