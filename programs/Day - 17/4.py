# Task:
# Create a parent class Number.
# Create SumNumber and ProductNumber classes that inherit from Number.
# Create a final class FinalCalculator that inherits from both.
# Call parent methods directly:
# SumNumber.sum(self, a, b).
# ProductNumber.product(self, a, b).
# Test:
# FinalCalculator().sum(5, 10) → 15
# FinalCalculator().product(3, 4) → 12

class Number:
    def __init__(self):
        pass

class Sum_number(Number):
    def sum(self, a, b):
        return a + b
    
class Product_number(Number):
    def product(self, a, b):
        return a * b

class FinalCalculator(Sum_number, Product_number):

    def sum(self, a, b):
        return Sum_number.sum(self, a, b)  
    def product(self, a, b):
        return Product_number.product(self, a, b)  
    
obj = FinalCalculator()
print(obj.sum(5,5))
print(obj.product(5,10))
