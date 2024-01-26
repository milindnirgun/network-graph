#!/bin/bash

# Usage:
# Source this script from .bashrc or equivalent.
# To use, run the command vworkon <virtual environment name>
# Note, the venv used must be present in the directory where this is command is executed.

function vworkon() {
    
    typeset env_name="$1"

    if [ "$env_name" == "" ]
    then
	echo "usage: vworkon <. | venv name>"	
	return 1
    elif [ "$env_name" = "." ]
    then
	# activate default venv in current directory
	# TODO - traverse thru directory hierachy to find a venv
	env_name="venv"
	export ENV_NAME=env_name
    fi
	
    echo "$env_name"
    #TODO- check if venv exists in current dir or somehow figure out path if this function is
    # invoked elsewhere
    activate="./$env_name/bin/activate"
    if [ ! -f "$activate" ]
    then
	echo "ERROR: Environment '$env_name' does not exist or contain an activate script." >&2
	return 1
    fi

    # Deactivate any current environment destructively before switching
    deactivate >/dev/null 2>&1

    source "$activate"

    return 0
}

