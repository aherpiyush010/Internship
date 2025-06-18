# 🔹 Part A: Functional Thinking
# 1.	Greeting Based on Time
# Define a function greet_user(hour) that:
# o	Takes current hour (24-hr format)
# o	Prints:
# 	"Good Morning" if 5–12
# 	"Good Afternoon" if 12–17
# 	"Good Evening" if 17–21
# 	"Good Night" otherwise

def greet_user(time):
    # time = int(input(" Enter current time (24-hr Format) : "))
    if time >= 5 and time < 12 :
        print(" -- Good Morning -- ")
    elif time >= 12 and time < 17 :
        print(" -- Good Afternoon -- ")
    elif time >= 17 and time < 21 : 
        print(" -- Good Evening -- ")
    else :
        print(" -- Good Night -- ")

greet_user(17)