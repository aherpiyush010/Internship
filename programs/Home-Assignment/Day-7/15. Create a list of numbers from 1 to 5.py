# 15.	Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.

divisible_by_3_and_5 = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)
