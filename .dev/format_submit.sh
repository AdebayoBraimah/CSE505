#!/usr/bin/env bash

# NOTE: Run this script/command from the .dev directory

chmod 755 ../report/cse-505-project/file_sub.py

zip -r file.zip <project>

../report/cse-505-project/file_sub.py -e project -e repository -e phase2 -f <file>

