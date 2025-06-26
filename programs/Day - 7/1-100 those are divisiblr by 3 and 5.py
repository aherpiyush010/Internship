# 1 -100 divisible by five 
list1 = []

for i in range(0,100):
    if i % 3 ==0 or i % 5 == 0:
        list1.append(i)
print(list1 , end = " ")