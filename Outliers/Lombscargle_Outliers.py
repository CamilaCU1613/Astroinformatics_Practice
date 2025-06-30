# import libraries
import matplotlib.pyplot as plt
import glob
import pandas as pd
from astropy.stats import sigma_clip
import numpy as np

# Find all .fits files in the current directory
fits_files = glob.glob("*.lc")

for filename in fits_files:
    # Upload the file, assuming it is a .txt or .lc file with space separators    
    df = pd.read_csv(filename, delim_whitespace=True)

    # Remove NaN
    df = df.dropna(subset=['PDCSAP_FLUX'])

    # Apply sigma clipping to detect outliers
    flux_clipped = sigma_clip(df['PDCSAP_FLUX'], sigma=3, maxiters=5)
    outliers = flux_clipped.mask  # Boolean mask: True = outlier

    # Plot
    plt.figure(figsize=(10, 5))
    
    # Plot normal points
    plt.errorbar(df['TIME'][~outliers], df['PDCSAP_FLUX'][~outliers], 
                 yerr=df['PDCSAP_FLUX_ERR'][~outliers], fmt='.', 
                 markersize=3, ecolor='gray', alpha=0.4, color='dimgray', label='Normal')

    # Plot outliers in red
    plt.errorbar(df['TIME'][outliers], df['PDCSAP_FLUX'][outliers], 
                 yerr=df['PDCSAP_FLUX_ERR'][outliers], fmt='o', 
                 markersize=4, color='red', alpha=0.8, label='Outliers')

    plt.xlabel('TIME / (BJD - 2457000), days')
    plt.ylabel('PDCSAP_FLUX / e-/s')
    plt.title(filename.replace("_lc.lc", ""))
    plt.grid(False)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename.replace("_lc.lc", "_outliers.png"))
    plt.show()
