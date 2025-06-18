#convert this string to dictionry 

str1 ="Hello welcome to rich system " 
length = str1.split()
dict1 = {i : len(i) for i in length}
print(dict1)
