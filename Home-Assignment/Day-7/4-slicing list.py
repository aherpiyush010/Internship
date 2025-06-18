# Part B: Slicing Lists
# 4.	Given numbers = [10, 20, 30, 40, 50, 60, 70], print:
# o	First 3 elements
# o	Last 2 elements
# o	Elements from index 2 to 5 (excluding 5)
# o	Reverse the list using slicing

numbers = [10, 20, 30, 40, 50, 60, 70]

print("First 3 elements:", numbers[:3])

print("Last 2 elements:", numbers[-2:])

print("Elements from index 2 to 5:", numbers[2:5])

print("Reversed list:", numbers[::-1])
