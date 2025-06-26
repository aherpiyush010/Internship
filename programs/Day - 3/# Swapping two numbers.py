# Swapping two numbers 
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
print(f"NUmbers before swapping : {num1}\t{num2}")

temp = num1
num1 = num2
num2 = temp


print(f"Numbers after swapping : {num1}\t{num2}")
