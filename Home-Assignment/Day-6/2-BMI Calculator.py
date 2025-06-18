# 2.    BMI Calculator
# Define a function calculate_bmi(weight, height) that:
# o	Takes weight in kg and height in meters
# o	Calculates BMI: bmi = weight / (height ** 2)
# o	Returns BMI and category:
# 	<18.5: Underweight
# 	18.5–24.9: Normal
# 	25–29.9: Overweight
# 	30+: Obese


    
def calculate_bmi(weight,height):
    weight = float(input("Enter your weight (kg) : "))
    height = float(input("Enter your height  (m)  : "))
    bmi = weight / (height ** 2)
    if bmi < 18.5 :
        category = "Underweight"
    elif bmi > 18.5 and bmi < 24.9 :
        category = "Normal"
    elif bmi > 25 and bmi < 29.9 :
        category = "Overweight"
    else : #bmi > 30  : 
        category = "Obese"
    print(f" BMI : {bmi} " )
    print(f" Category : {category} " )
    return category,bmi

calculate_bmi(weight,height)