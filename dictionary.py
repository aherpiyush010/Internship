original = {'a': 1, 'b': 2, 'c': 1}
inverted = {}

for key, value in original.items():
    if value not in inverted:
        inverted[value] = []
    inverted[value].append(key)

print(inverted)



