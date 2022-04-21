# class initalization 
# Employee class is called super class 
class Employee:
    def __init__(self,first_name, last_name,salary, shift):
        self._first_name=first_name   # _ meant private but visiable or technically called Encapulation
        self._last_name=last_name
        self.salary=salary 
        self.shift=shift

    
    # class function
    def get_fullname(self):
        return f'{self._first_name} {self._last_name}'  # Encapulation
        
# inheritance from  parent class , create subclasses based on job title
class Mechanic(Employee):
    job_title="Mechanic"   # class variable: Shared between All instances of the class 
  
class Attdendant(Employee):
    job_title="Station Attendant"

class Cook(Employee):
    job_title="Cook"

class Manager(Employee):
    job_title="Manager"
