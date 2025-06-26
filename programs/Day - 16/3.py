# Create a Car Class
# Attributes:
# brand (string), model (string), speed (initially 0).
# Methods:
# accelerate() — Increases speed by 10
# brake() — Decreases speed by 5
# display_speed() — Shows the current speed
# Test it: Create a car object, call accelerate() and brake() a few times, and display the speed
class Car:
    def __init__( self , brand , model , Speed ):
        self.brand = brand
        self.model = model
        self.speed = Speed
        
    def accelerate(self):
        self.inc = self.speed = self.speed + 10
    
    def brake(self):
        self.de = self.speed = self.speed - 5
        
    def output(self):
        print("The brand of car is : ",self.brand)
        print("The model of car is : ",self.model)
        print(" Your current speed is : ", self.speed)

car = Car('bmw' , 'M1' ,0)
car.output()
car.accelerate()
car.accelerate()
car.output()
car.brake()
car.output()