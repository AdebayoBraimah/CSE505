#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# DESCRIPTION:
# 
# Intended for building sphinx documentation
#   locally.

cwd=$(pwd)
wd=$(dirname $(realpath ${0}))

cd ${wd}

sphinx-apidoc -o source ../src

make clean; make html

cd ${cwd}
