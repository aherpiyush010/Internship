#write a python program to dict {'a':1, 'b':2, 'c':1} convrt the key into value 
dict ={'a':1, 'b':2, 'c':1}
dict2 = {}
for k,v in dict.items():
    if v in dict2:
        dict2[v].append(k)
    else:
        dict2[v] = [k]
        
print(dict2)