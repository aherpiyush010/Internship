# 14. Create a multiplication table from 1 to 5, like:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 10 = 50

no = int(input(" Enter the number : "))

for i in range(1,11) : 
    for j in range(1,no+1) :
        k = i * j
        print(f" {i} X {j} = {k} ",end='\t')
    print()


