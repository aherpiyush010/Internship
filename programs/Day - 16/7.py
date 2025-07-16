# Calculator Class with Static Methods
# Create a Calculator class:
# add(a, b) — Static method
# multiply(a, b) — Static method
# is_even(number) — Static method
# Test it: Call these methods without creating an object, like:
# Calculator.add(5, 3)  # Returns 8

class calculator:
    @staticmethod
    def add(a, b):
        print("The sum of two numbers is : ",a+b)
    @staticmethod
    def mul(a, b):
        print("multiplication : ", a*b)
        
    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            print("your number is even ..")
        else:
            print("number is odd ..")
calculator.add(5,2)
        
        
    