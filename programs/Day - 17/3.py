# Task: Multilevel Inheritance
# Create a class Number:
# Attribute: value.
# Create a class SquareNumber that inherits from Number:
# Method: square() → returns value * value.
# Create a class CubeNumber that inherits from SquareNumber:
# Method: cube() → returns value * value * value.
# Test:
# Number(2) → value = 2
# SquareNumber(3).square() → 9
# CubeNumber(3).cube() → 27

class Number:
    def __init__(self, value):
        self.value = value

class Square_Number(Number):
    def Square(self):
        return self.value ** 2
    
class Cube_number(Square_Number):
    def cube(self):
        return self.value ** 3

obj = Cube_number(3)
print(" Number we entered : ", obj.value)
print(f" Square of {obj.value} is : {obj.Square()}")
print(f" cube of {obj.value} is : {obj.cube()}")
    