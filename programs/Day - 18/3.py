# Partially Implemented Abstract Class
# # Instructions:
# Create an abstract class named Employee:
# Abstract method: calculate_salary().
# Concrete method: display_role() (prints role).
# Create concrete classes:
# FullTimeEmployee with a calculate_salary() method.
# PartTimeEmployee with a calculate_salary() method.
# Instantiate both and test both methods.

from abc import ABC, abstractmethod 
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_role(self):
        print("Manager")
        
class FullTimeEmployee(Employee):
    def calculate_salary(self,salary):
        print("Full Time Employee salary is : ",salary)
class PartTimeEmployee(Employee):
    def calculate_salary(self,salary):
        print("Part time Employee salary is : ",salary)
        
fe = FullTimeEmployee()
pe = PartTimeEmployee()
fe.display_role()
fe.calculate_salary(50,000)
pe.calculate_salary(20,000)