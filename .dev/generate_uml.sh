#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# DESCRIPTION: Create UML diagrams from python code.
# 
# DEPENDENCIES: pylint/pyreverse
# 
# Example usage: ./generate_uml.sh -p ../src -o ../docs/source/uml

#######################################
# Prints usage to the command line interface.
# Arguments:
#   None
#######################################
Usage(){
  cat << USAGE

  Usage:

      $(basename ${0}) -p <package path> [-o <output directory>]

  Required arguments
    -p, --package                     Package directory or module file path
  
  Optional arguments
    -o, --output, --output-directory  Output directory name
    -h, -help, --help                 Prints the help menu, then exits.

USAGE
  exit 1
}


#######################################
# Prints message to the command line interface
#   in some arbitrary color.
# Arguments:
#   msg
#######################################
echo_color(){
  msg='\033[0;'"${@}"'\033[0m'
  echo -e ${msg}
}


#######################################
# Prints message to the command line interface
#   in red.
# Arguments:
#   msg
#######################################
echo_red(){
  echo_color '31m'"${@}"
}


#######################################
# Prints message to the command line interface
#   in green.
# Arguments:
#   msg
#######################################
echo_green(){
  echo_color '32m'"${@}"
}


#######################################
# Prints message to the command line interface
#   in blue.
# Arguments:
#   msg
#######################################
echo_blue(){
  echo_color '36m'"${@}"
}


#######################################
# Prints message to the command line interface
#   in red when an error is intened to be raised.
# Arguments:
#   msg
#######################################
exit_error(){
  echo_red "${@}"
  exit 1
}


main(){
  #
  # Parse arguments
  #============================

  # Check arguments
  if [[ ${#} -lt 1 ]]; then
    Usage >&2
    exit 1
  fi

  # Set defaults
  local out=""

  while [[ ${#} -gt 0 ]]; do
    case "${1}" in
      -p|--package) shift; local package=${1} ;;
      -o|--output|--output-directory) shift; local out=${1} ;;
      -h|-help|--help) Usage; ;;
      -*) echo_red "$(basename ${0}): Unrecognized option ${1}" >&2; Usage; ;;
      *) break ;;
    esac
    shift
  done

  #
  # Dependency checks
  #============================

  if ! hash pyreverse 2>/dev/null; then
    exit_error "pylint/pyreverse is not installed. Please check. Exiting..."
  fi

  #
  # Check arguments
  #============================

  if [[ -z ${package} ]] || [[ ! -d ${package} ]] && [[ ! -f ${package} ]]; then
    exit_error "Package was not specified or does not exist. Exiting..."
  else
    package=$(realpath ${package})
    package_name=$(basename ${package})
  fi

  #
  # Make output directory
  #============================

  if [[ ! -z ${out} ]] && [[ ! -d ${out} ]]; then
    mkdir -p ${out}
    out=$(realpath ${out})
  elif [[ -d ${out} ]]; then
    out=$(realpath ${out})
  fi

  #
  # Create UML Diagram
  #============================

  if [[ ! -z ${out} ]]; then
    cmd="--output-directory=${out}"
  else
    cmd=""
  fi

  pyreverse --output png --project ${package_name} ${package} ${cmd}
}

# Execute main function
main "${@}"
