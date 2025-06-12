# 7- 	Ask the user to enter their name and age. Print how many years are left until they turn 100.
# Example:
# Enter your name: Anjali
# Enter your age: 25
# Output: Hello Anjali, you will turn 100 in 75 years!

name = input(" Enter your name : ")
age = int(input(" Enter your age : "))
rem_age = 100 - age

print(f" Hello {name}, you will turn 100 in {rem_age} years")