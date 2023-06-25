#!/bin/bash

if [ $# != 2 ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi
year=$1
day=$(printf "%02d" "$2")

mkdir -p "$year/$day"
if [ -e "$year/$day/$day.py" ]; then
    echo "$day.py already exists!"
    exit 1

fi
cp ./base.py "$year/$day/$day.py"
touch "$year/$day/example"
touch "$year/$day/input"
