#!/usr/bin/env bash

# Measure size of code base
# 
# Found from the following link: https://stackoverflow.com/a/48254241

# NOTE: This script/command must be run from the root of the project
# 
# cd /Users/adebayobraimah/Desktop/projects/CSE505
# git ls-files | xargs wc -l
# 
# Done!

# Measure the code base
git ls-files | xargs wc -l