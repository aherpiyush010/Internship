# 16.	Write a program that takes 5 numbers from the user and stores them in a list. Then:
# •	Print the sum
# •	Print the max and min number
# •	Sort the list and print it

# Take 5 numbers from the user and store them in a list
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1} : "))
    numbers.append(num)
print(" Unsorted list :", numbers)

# Print the sum of the numbers
total = sum(numbers)
print(" Sum :", total)

# Print the maximum and minimum numbers
print(" Maximum number in list :", max(numbers))
print(" Minimum number in list :", min(numbers))

# Sort the list and print it
numbers.sort()
print(" Sorted list :", numbers)
