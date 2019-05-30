#!/bin/bash

FILE_PATH=$(python export.py)
source $FILE_PATH
echo $MONGO_PATH
