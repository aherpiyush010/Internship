# numbers greater than one 
 
my_tuple = (1,2,7,4,2,9,2,6,2,8,4,8,4,6,2,)

list1 = []
for i in my_tuple :
    if my_tuple.count(i) > 1 and i  not in list1 :
        list1.append(i)
        print(my_tuple.count(i))
        

print(list1)
print
