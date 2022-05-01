Prerequisites for building and testing SciPy project on macOS:
1.	Installation of official Python distribution.
2.	Installation of Homebrew and GNU FORTRAN compiler via Homebrew. Cython and Pythran compilers are also required.
3.	Installation of OpenBLAS library providing the BLAS and LAPACK interfaces.
4.	Download the latest release from https://github.com/scipy/scipy.

To reproduce enviroment, we need to run `pip install -r doc_requirements.txt -r mypy_requirements.txt`

Code coverage can be run by installing the coverage tool using pip and running the following commands: 
`$ coverage run runtests.py` 
`$ coverage json -o OUTFILE`

