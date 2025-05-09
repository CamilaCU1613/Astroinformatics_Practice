#!/bin/bash
# This script splits a text file into 5 line 

# Splits the file: each new file will have 5 lines.
split -l 5 csv_file_list.txt csv_split_

# Displays output.
echo "Split file:"
ls csv_split_*


