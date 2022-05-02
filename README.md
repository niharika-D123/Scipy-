## Prerequisites for building and testing SciPy project on macOS:
1.	Installation of official Python distribution.
2.	Installation of Homebrew and GNU FORTRAN compiler via Homebrew. Cython and Pythran compilers are also required.
3.	Installation of OpenBLAS library providing the BLAS and LAPACK interfaces.
4.	Download the latest release from https://github.com/scipy/scipy.

To reproduce enviroment, we need to run `pip install -r doc_requirements.txt -r mypy_requirements.txt`

Code coverage can be run by installing the coverage tool using pip and running the following commands: 

`$ coverage run runtests.py`

`$ coverage json -o OUTFILE`

## Details about files:

a. coverage.json: This is the code coverage report generated in json format.

b.coverage.pdf : This is the code coverage reported generated from html to pdf.

c. task2.py: This file contains the script to find the total number of test files and the number of assert statements in each file.

d. tak3.py: This file contains the script to find the location,file and number of times debug  statements has appeared in the production files.

e. task3_2.py:This file contains the scripts to find the location,file and the number of times assert statements has appeared in the production files.

f. task4.py: This file contains the scripts to find when test files are added,modified to this project and by whom, within last six months.

g. gen-figures.py: This script was used to plot the figures.
