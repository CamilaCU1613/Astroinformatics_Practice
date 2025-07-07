In this repository, you will find the solutions to practices 1-4 corresponding to the Astroinformatics 2025-1 course. The objective of this project is data processing, structuring Python and .sh functions, and mapping light curves from the TESS project. Ungraded preliminary solutions are located in the Ungraded_practice folder, while graded solutions are located in the Graded_Practice folder.

- In the FITS_File folder, you will find the 20 files obtained from the first point of the practical session on the MAST platform, along with their downloadable .sh file.
- In the CSV Files folder, you will find the .fits files converted to .csv format in Topcat, corresponding to point two of the practical session.
- In the CSV_list folder, you will find the script with the commands to generate a text file with the list of names of the .csv files corresponding to the solution to point three of the practical session. Meanwhile, in the CSV_File folder, you will find the converted files with this extension for the light curves.
- In the Splitting folder, you will find the split files and the script to generate them as the solution to point four of the practical session.
- In the Light_curve folder, you will find the images extracted from Topcat as the solution to point five of the practical session.
- In the LC_File folder, you will find the code and the .lc files associated with the light curves.
- In the Spectra_class and Julian_day folders, you will find the Python codes corresponding to tasks 1 and 2 of Practical Session 2. Here, each function has its multi-line docstring explaining how it works.
- In the LightCurve_python folder, you will find the light curves plotted with matplotlib and saved as .PNG files corresponding to the solution to Practice 3.
- In the Outliers folder, you will find the py code and PNG images for detecting anomalous points within the light curves using the astropy library.
- In the Statistical_Analysis folder, you will find the statistical steps performed to build the analysis on the light curves in Practice 3. Here, you will find the periograms found with Lombscargle from the astropy library and the light curves phased with respect to time.

TEST CASE IDENTIFICATION:

When processing TESS light curves, it is critical to consider various edge cases that can generate errors or affect data quality. For example, missing or corrupted data can generate NaN values ​​or malformed matrices during analysis. Period detection can fail or generate erroneous results when the light curve is too short or sampled irregularly. Outlier detection could misclassify valid variability as noise, especially during transits. Additionally, file handling errors can occur if the directory structure is incorrect or file names are misspelled. Finally, it is important to detect invalid input values ​​(e.g., negative flow, non-numeric timestamps, or empty files) early to avoid silent failures in graphs or statistical operations.

Example:
___________________________________________________________________________________________
df = pd.read_csv("empty_lightcurve.csv") # Empty file
print(df.head()) # Error or empty data frame breaking further analysis

flux = np.array([1.2, 1.3, np.nan, 1.5])
mean_flux = np.mean(flux) # Result will be NaN if not filtered

t = np.array([1, 2]) # Only two points
y = np.array([0.9, 1.0])
frequency, power = LombScargle(t, y).autopower() # May fail or warn

flux = np.array([1.1, -0.5, 1.3]) # Negative flux values
if np.any(flux < 0):
print("Warning: Negative flux values ​​detected.") # This could indicate a preprocessing error

with open("lightcurve_typo.csv", "r") as f:
data = f.read() # FileNotFoundError if the file does not exist

df = pd.DataFrame({'time': ['a', 'b', 'c'], 'flux': [1.0, 1.1, 1.2]})
df['time'] = pd.to_numeric(df['time']) # ValueError: Unable to parse string "a"

______________________________________________________________________________________________

IMPLEMENTATION

Each of the .sh or py files has its implementation instructions, which basically consist of accessing the TESS-MAST project data in the following form:

From STScI's Mikulski Archive, download light curves from the TESS satellite. To do so, go to https://archive.stsci.edu/tess/bulk_downloads/bulk_downloads_ffi-tp-lc-dv.html.
Download this script and run it: tesscurl sector 73 lc.sh
The script will download light curve files in FITS format. 

This will simply run each of the codes in the order described in the labs, allowing you to switch from .csv to .lc files to directly graph the light curves. You can also clone the repository along with the dependencies without having to download the data directly from TESS by running:
__________________________________________________________________
git clone https://github.com/yourusername/astroinformatics2025.git
___________________________________________________________________

Install the required dependencies from the requirements.txt file:
_______________________________
pip install -r requirements.txt
_______________________________


CREDITS

Developed by: Camila Cárdenas Uribe
Course: Astroinformatics 2025-1
Instructor: Nina Hernitschek
Institution: University of Antofagasta
