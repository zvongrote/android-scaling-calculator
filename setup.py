import setuptools

# Package meta-data
NAME = 'scaling-calculator'
VERSION = '1.0'
DESCRIPTION = 'Calculates scaled dimensions for a list of given pixel densities'
REQUIRES_PYTHON = '>=3.9.0'
REQUIRED = []
PACKAGES = []

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    install_requires=REQUIRED,
    packages=PACKAGES,
    python_requires=REQUIRES_PYTHON
)