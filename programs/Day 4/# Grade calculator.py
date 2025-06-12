# Grade calculator 
sub1 = int(input("Enter the marks of First subject :"))
sub2 = int(input("Enter the marks of Second subject :"))
sub3 = int(input("Enter the marks of Third subject :"))
sub4 = int(input("Enter the marks of Fourth subject :"))
sub5 = int(input("Enter the marks of Fifth subject :"))

Total = sub1+sub2+sub3+sub4+sub5
Percentage = (Total*100)/500

if Percentage>75 :
    print("Grade : A")
    
elif Percentage>60 or Percentage<75:
    print("Grade : B")
    
elif Percentage>50 or Percentage<60:
    print("Grade : C")
    
elif Percentage>40 or Percentage<50:
    print("Grade : D")
    
else: 
    print("Grade : Fail")
    
print("-----Result-----")
print(f"Marks of subject 1 : {sub1}")
print(f"Marks of subject 2 : {sub2}")
print(f"Marks of subject 3 : {sub3}")
print(f"Marks of subject 4 : {sub4}")
print(f"Marks of subject 5 : {sub5}")
print(f"Average : {Percentage}")
