#!/bin/sh

# Get dir of the script
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PYTHONPATH=$DIR/../ python $DIR/datapoint.py
