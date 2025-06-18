# 12.	Remove an element from a set using remove() and discard().
# •	Try removing an element that doesn’t exist using both.

s1 = {1, 2, 3, 4, 5}
print(s1)
# Remove an element using remove()
s1.remove(1)
print("Set after removing 1 using remove():", s1)
s1.discard(2)
print("Set after removing 2 using discard():", s1)

