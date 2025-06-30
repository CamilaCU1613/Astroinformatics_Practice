import matplotlib.pyplot as plt
import glob
import pandas as pd
import numpy as np
from astropy.timeseries import LombScargle

# Find all .lc files in the current directory
fits_files = glob.glob("*.lc")

for filename in fits_files:
    # Upload the file
    df = pd.read_csv(filename, sep=r"\s+")

    # Remove NaN
    df = df.dropna(subset=['PDCSAP_FLUX'])

    # Basic statistics
    amplitude = df['PDCSAP_FLUX'].max() - df['PDCSAP_FLUX'].min()
    std_dev = df['PDCSAP_FLUX'].std()
    print(f"\n{filename}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    time = df['TIME']
    flux = df['PDCSAP_FLUX']

    # Lomb-Scargle periodogram
    frequency, power = LombScargle(time, flux).autopower()
    best_frequency = frequency[np.argmax(power)]
    period = 1 / best_frequency
    print(f"Period: {period:.8f} days")

    # Phase folding
    phase = (time % period) / period
    phase_double = np.concatenate([phase, phase + 1])
    flux_double = np.concatenate([flux, flux])

    # Plot both periodogram and folded light curve
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=False)

    # Periodogram
    axs[0].plot(1 / frequency, power, color='blue', lw=1)
    axs[0].axvline(period, color='red', linestyle='--', label=f'Best period = {period:.5f} d')
    axs[0].set_xlabel('Period (days)')
    axs[0].set_ylabel('Lomb-Scargle Power')
    axs[0].set_title(f'Lomb-Scargle Periodogram: {filename.replace("_lc.lc", "")}')
    axs[0].legend()
    axs[0].grid(True)

    # Folded light curve
    axs[1].scatter(phase_double, flux_double, s=5, alpha=0.6, color='black')
    axs[1].set_xlabel('Phase')
    axs[1].set_ylabel('PDCSAP_FLUX / e-/s')
    axs[1].set_title(f'Phase-folded Light Curve: {filename.replace("_lc.lc", "")}')
    axs[1].grid(True)

    # Save figure
    output_filename = filename.replace("_lc.lc", "_analysis.png")
    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.close()

    print(f"Saved: {output_filename}")
