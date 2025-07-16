# creating a tuple 

my_tuple = ("apple","banana","mango")
length = []
for i in my_tuple :
     length.append(len(i))
A = tuple(length)
print(A)
print(my_tuple)