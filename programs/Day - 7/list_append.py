list1 = []

for i in range(1,11):
    list1.append(int(input(f" Enter number {i}  : ")))
print(list1)
    
for i in range(len(list1)):
     list1[i] = list1[i]**2
print(list1)