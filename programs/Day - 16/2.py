# Create a Rectangle Class
# Attributes: length, width.
# Methods:
# area() — Returns the area of the rectangle.
# perimeter() — Returns the perimeter.
# Test it: Create a few instances and print their area and perimeter

class Rectangle:
    def __init__( self , len , wid ):
        self.len = len
        self.wid = wid
    
    def area(self):
        self.Area = self.len * self.wid
        
    def perimeter(self):
        self.peri = 2 * ( self.len + self.wid )
        
    def output(self):
        self.area()
        self.perimeter()
        print(" The area of rectangle is : ",self.Area)
        print(" The perimeter of rectangle is : ",self.peri)
        
obj = Rectangle(13,5)
obj1 = Rectangle(12,4)
obj2 = Rectangle(3,2)
obj.output()
obj1.output()
obj2.output()