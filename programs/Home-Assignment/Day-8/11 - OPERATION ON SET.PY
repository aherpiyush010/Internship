# 11.	Given:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Perform and print:
# •	Union of a and b
# •	Intersection of a and b
# •	Difference: a - b and b - a

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}    
print("Set a:", a)
print("Set b:", b)
# Union of a and b
s1 = a.union(b)       
print("Union of a and b:", s1)
# Intersection of a and b
s2 = a.intersection(b)
print("Intersection of a and b:", s2)
# Difference: a - b
s3 = a.difference(b)
print("Difference a - b:", s3)
