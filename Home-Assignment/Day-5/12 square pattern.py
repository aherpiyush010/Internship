# 12.	Print a square pattern using nested for loops:
# * * * *
# * * * *
# * * * *
# * * * *

rows = columns = int(input("Enter number of rows & column : "))

for i in range(rows):
    for j in range(columns):
        print('*', end=' ')
    print()
