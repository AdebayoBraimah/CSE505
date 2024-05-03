#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

_PKG_PATH: str = "/Users/adebayobraimah/Desktop/projects/CSE505"

sys.path.append(_PKG_PATH)


from src import RESROURCEDIR
from src.kg.knowledge_graph import scrape_sbu_solar, KnowledgeGraph
from src.ergoai.ergoai import json_to_ergo
from src.clapi.clapi import process_course_data_clingo


url = "https://prod.ps.stonybrook.edu/psc/csprodg/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?"


majors = (
    "cse",
    # "ams",
    # "bio",
    # "phy",
    # "ast",
    # "mat",
    # "che",
    # "geo",
    # "ise",
    # "wrt",
    # "bme",
    # "esg",
    # "ese",
    # "mec",
    # "psy",
)

for major in majors:
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
    else:
        pass

    if not (os.path.exists(f"{outname}_courses.lp")):
        process_course_data_clingo(
            file_path=f"{outname}_courses.json", output_file=f"{outname}_courses.lp"
        )
