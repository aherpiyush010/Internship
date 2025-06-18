# 🔹 Part E: Code & Scope Logic
# 11.	Local vs Global Debugging
# Create a global variable x = 50
# •	Define function that modifies x locally
# •	Define another that uses global x
# •	Print x before and after both functions


x = 50

def modify_local():
    x = 100  
    print("Inside modify_local, x =", x)

def modify_global():
    global x     
    x = 200
    print("Inside modify_global, x =", x)


print("Before functions, x =", x)

modify_local()   
print("After modify_local, x =", x)

modify_global()  
print("After modify_global, x =", x)
