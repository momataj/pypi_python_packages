# pypi_python_packages
Developing custom python packages for varies use cases.

## create pypi packages

 python setup.py bdist_wheel

 ## upload pypi packages into the respository 

twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

## Packages:
* pip install s3-upload-download


## OOP
##
- Classes and Objects
- Inheritance 
- Encapsulation
- Polymorphism 
- Composition 
- Unit Testing

### UML Universal Modeling langauage 

.. code-block:: python
    Class Name -> Employee
    Attribute -> Name
                Salary 

    Methods -> __init__(str,num)

Turn UML to python code: 

.. code-block:: python

    class Employee:
        def __init__(self,name,salary):
            self.name=name
            self.salary=salary 
