# count of character in a string

count = 0
def my_function():
    global count
    Sentence = " Hello i am piyush i study in k k wagh institute of technology "
    for i in Sentence :
        if i == "i":
            count += 1   
    print(count)

my_function()