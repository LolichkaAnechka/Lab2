# Lab 2. Part 1
# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter and 
# the area of the rectangle. Also, provide setter and getter for the length and width attributes. The setter should verify that length and width 
# are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    def __init__(self, lenght=1, width=1):
        if not (isinstance(lenght, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("Wrong value type")

        if not (lenght > 0 and width >0):
            raise ValueError("Wrong value")

        self.lenght, self.width=lenght, width

    
    def area(self):
        return self.width*self.lenght

    def perimeter(self):
        return 2*(self.width + self.lenght)
    

    def getData(self):
        return {'lenght': self.lenght, 'width': self.width}
    

    def setLenght(self, newlenght):
        if not (newlenght >= 0.0 and newlenght <=20.0):
            raise ValueError("Wrong value")
        self.lenght = newlenght
            
    
    def setWidth(self, newwidth):
        if not(newwidth >= 0.0 and newwidth <=20.0):
            raise ValueError("Wrong value")
        self.width = newwidth
            

x = Rectangle()
print(x.getData())
a = Rectangle(13, 15)

print(a.area())
print(a.perimeter())
a.setLenght(20.1)
a.setWidth(18)
print(a.getData())
print(a.getData())

b= Rectangle(-5, -5)
