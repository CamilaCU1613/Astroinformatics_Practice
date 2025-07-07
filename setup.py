from setuptools import setup, find_packages

setup(
    name="Astroinformatics_Practice",
    version="0.1.0",
    description="TESS light curve analysis for the Astroinformatics 2025-1 course",
    author="Camila Cárdenas Uribe",
    author_email="camila.cardenas.uribe@uamail.cl",
    url="https://github.com/CamilaCU1613/Astroinformatics_Practice.git", 
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "glob",
        "astropy",
        "scipy",
        "setup"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # O la que uses
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
