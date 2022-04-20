# pypi_python_packages
Developing custom python packages for varies use cases.

## create pypi packages

 python setup.py bdist_wheel

 ## upload pypi packages into the respository 

twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

## Packages:
* pip install s3-upload-download