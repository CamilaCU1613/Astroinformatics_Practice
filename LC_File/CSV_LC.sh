#!/bin/bash
# Loop through all files endingin .csv
for archive in *.csv; do
    # Create a new file name
    # with a .lc extension
    new_archive="${archive%.csv}.lc"

    # Replace commas with spaces
    awk -F',' '
    # Extract the columns
    BEGIN {
        OFS = " "
    }
    NR==1 {
        for (i = 1; i <= NF; i++) {
            gsub(/^ +| +$/, "", $i)  #remove leading/trailing spaces
            if ($i = = "TIME") time= i
            if ($i = = "PDCSAP_FLUX") flux = i
            if ($i = = "PDCSAP_FLUX_ERR") err=i
        }
    }
    NR > 1 && time && flux && err {
        print $time, $flux, $err
    }
    ' "$archive" > "$new_archive"

    echo "File: $archive -> $new_archive"
done
