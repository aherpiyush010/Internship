# updating a gllobal variable

count = 0
def my_function():
    
    global count 
    count += 2
    print(count) 
my_function() 