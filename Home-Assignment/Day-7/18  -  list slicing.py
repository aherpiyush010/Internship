# 18.	Given sentence = "Python is powerful", convert it into a list of words and then reverse the list using slicing.

sentence = "Python is powerful"

# Convert the sentence into a list of words
l1 = sentence.split()

# Reverse the list using slicing
l2 = l1[::-1]

print(l2)
