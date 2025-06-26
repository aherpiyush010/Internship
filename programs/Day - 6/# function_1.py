# Arithmetic operation using function

def my_function():
    
    num1 = int(input(" Enter first number : "))
    num2 = int(input(" Enter second number : "))
    operator = input(" Enter operator you want to perform operation (+,-,/,*) : ")
    
    if operator == "+":
        print(f"Addition of {num1} and {num2} is {num1+num2}")
    elif operator == "-":
        print(f"Substraction of {num1} and {num2} is {num1-num2}")
    elif operator == "*":
        print(f"Multiplication of {num1} and {num2} is {num1*num2}")
    elif operator == "/":
        print(f"Division of {num1} and {num2} is {num1/num2}")
    else:
        print("invalid choice ... ")

my_function()