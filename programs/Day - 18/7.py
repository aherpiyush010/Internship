# Task: Property Decorators
# Instructions:
# Create a class Student.
# Private attribute: __name.
# Use @property for getting the name.
# Use @name.setter for setting the name, ensuring it’s not an empty string.
# Try creating instances and setting names.

class Student:
    def __init__(self, name):
        self.__name = None  
        self.name = name    

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            print("Empty string is not allowed  ")
        else:
            self.__name = value
            print(self.__name)
            
s = Student("")
s.name
