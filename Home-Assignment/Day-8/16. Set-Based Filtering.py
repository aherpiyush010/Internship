# 16.	Set-Based Filtering
# o	Ask user to enter 5 numbers (some duplicates allowed)
# o	Store them in a list
# o	Use a set to display only unique numbers


numbers = []
print("Enter 5 numbers (duplicates allowed):")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

unique_numbers = set(numbers)

print("Unique numbers are:")
print(unique_numbers)
