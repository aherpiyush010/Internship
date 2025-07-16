# Tasks on Encapsulation
# Task: Private Attribute and Method
# Instructions:
# Create a class Car.
# Add a private attribute __speed.
# Create a method accelerate(value) to increase the __speed.
# Create a method get_speed() to return the current __speed.
# Try accessing __speed directly (and understand why it doesn’t work).

class Car:
    def __init__(self):
        self.__speed = self.no = 10 

    def accelerate(self, value):
        if value > self.no:
            self.__speed += value
            print(f"Accelerated by {value}.")
        else:
            pass

    def get_speed(self):
        return self.__speed

my_car = Car()

my_car.accelerate(100)
print("Current speed:", my_car.get_speed())  

