# 15.	Immutable Data Storage
# o	Store employee data as:
# employee = ("John", "Manager", 55000)
# o	Try adding a new field to this tuple. What happens?

# Immutable data storage
employee = ("John", "Manager", 55000)

employee.append("New York")  

# output : 
#     AttributeError: 'tuple' object has no attribute 'append'
