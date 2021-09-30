# Lab 2. Part 1
# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter and 
# the area of the rectangle. Also, provide setter and getter for the length and width attributes. The setter should verify that length and width 
# are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    def __init__(self, lenght=1, width=1):
        if isinstance(lenght, (int, float)) and isinstance(width, (int, float)):
            if lenght > 0 and width >0:
                self.lenght=lenght
                self.width=width
            else:
                raise ValueError("Wrong value")
        else:
            raise TypeError("Wrong value type")

    
    def area(self):
        return self.width*self.lenght

    def perimeter(self):
        return 2*(self.width + self.lenght)
    
    def getLenght(self):
        return self.lenght

    def getWidth(self):
        return self.width
    
    def setLenght(self, len):
        if len >= 0.0 and len <=20.0:
            self.lenght = len
        else:
            raise ValueError("Wrong value")
    
    def setWidth(self, wid):
        if wid >= 0.0 and wid <=20.0:
            self.width = wid
        else:
            raise ValueError("Wrong value")

x = Rectangle()
x.getLenght
a = Rectangle(13, 15)

print(a.area())
print(a.perimeter())
a.setLenght(20.1)
a.setWidth(18)
print(a.getLenght())
print(a.getWidth())

b= Rectangle(-5, -5)