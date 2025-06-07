#!/bin/bash

# Loop through all files ending in .csv
for archive in *.csv; do
    # Create a new file name with a .lc extension
    new_archive="${archive%.csv}.lc"

    # Replace commas with spaces
    awk -F',' '
    # Extract only the TIME and PDCSAP_FLUX columns
    BEGIN {
        OFS = " "
    }
    NR==1 {
        for (i = 1; i <= NF; i++) {
            if ($i == "TIME") time_col = i
            if ($i == "PDCSAP_FLUX") flux_col = i
        }
    }
    {
        print $time_col, $flux_col
    }
    ' "$archive" > "$new_archive"

    echo "File processing: $archive -> $new_archive"
done



