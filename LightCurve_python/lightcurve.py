# import libraries
import matplotlib.pyplot as plt
import glob

# Find all .fits files in the current directory
fits_files = glob.glob("*.lc")

for filename in fits_files:
    # Upload the file, assuming it is a .txt or .lc file with space separators    
    df = pd.read_csv(filename, delim_whitespace=True)
    
    # remove NaN
    df = df.dropna(subset=['PDCSAP_FLUX'])
    
    # plot
    plt.figure(figsize=(10, 5))
    plt.errorbar(df['TIME'], df['PDCSAP_FLUX'], yerr=df['PDCSAP_FLUX_ERR'], markersize=3, fmt='.', ecolor='gray', alpha=0.4, color='dimgray')
    plt.xlabel('TIME/BJD - 2457000, days)')
    plt.ylabel('PDCSAP_FLUX/ e-/S')
    # remove the .lc extension from the object name
    plt.title(filename.replace("_lc.lc", ""))
    plt.grid(False)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename.replace("_lc.lc", ".png"))
    plt.show()
    print(f"Save: {filename.replace("_lc.lc", ".png")}")
    
