#!/bin/bash

if [ $# != 2 ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi
year=$1
day=$(printf "%02d" "$2")

mkdir -p "python/$year/$day"
if [ -e "python/$year/$day/$day.py" ]; then
    echo "$day.py already exists!"
    exit 1

fi
cp ./base.py "python/$year/$day/$day.py"
touch "python/$year/$day/example"
touch "python/$year/$day/input"
