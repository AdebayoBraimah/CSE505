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
parallel -j 4 < ${job_file}
