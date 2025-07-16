# 17.	Create a list names = ["Alice", "Bob", "Charlie", "David"]
# •	Use list comprehension to create a list of name lengths: [5, 3, 7, 5]

names = ["Alice", "Bob", "Charlie", "David"]


name_lengths = [len(name) for name in names]

print(name_lengths)
