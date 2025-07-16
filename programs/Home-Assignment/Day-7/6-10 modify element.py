# 🔹 Part C: Modifying Elements
# 6.	Replace the third element of a list marks = [45, 67, 89, 34] with 99.
# 7.	Add an element "python" at the end of a list languages = ["C", "Java"].
# 8.	Insert "HTML" at index 1 in the above list.
# 9.	Remove the last item using pop() and print it.
# 10.	Delete the second element using del.

# 6. Replace the third element with 99
marks = [45, 67, 89, 34]
marks[2] = 99
print("Updated marks:", marks)  # Output: [45, 67, 99, 34]

# 7. Add "python" at the end
languages = ["C", "Java"]
languages.append("python")
print("After append:", languages)  # Output: ["C", "Java", "python"]

# 8. Insert "HTML" at index 1
languages.insert(1, "HTML")
print("After insert:", languages)  # Output: ["C", "HTML", "Java", "python"]

# 9. Remove the last item using pop() and print it
removed = languages.pop()
print("Popped item:", removed)
print("After pop:", languages)

# 10. Delete the second element using del
del languages[1]
print("After deleting second element:", languages)
