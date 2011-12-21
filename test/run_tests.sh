#!/bin/sh

# Get dir of the script
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PYTHONPATH=$DIR/../ python $DIR/datapoint.py
#PYTHONPATH=$DIR/../ python $DIR/session.py
PYTHONPATH=$DIR/../ python $DIR/cursor.py
PYTHONPATH=$DIR/../ python $DIR/collection.py
PYTHONPATH=$DIR/../ python $DIR/database.py
PYTHONPATH=$DIR/../ python $DIR/naming.py
