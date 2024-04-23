#!/usr/bin/env bash

# Measure size of code base
# 
# Found from the following link: https://stackoverflow.com/a/48254241

# TODO: Write instructions and details later

# NOTE: This script/command must be run from the root of the project

# Measure the code base
git ls-files | xargs wc -l