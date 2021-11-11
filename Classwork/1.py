# Lab 2. Part 1
# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter and 
# the area of the rectangle. Also, provide setter and getter for the length and width attributes. The setter should verify that length and width 
# are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    def __init__(self, new_lenght=1, new_width=1):
        if not (isinstance(new_lenght,(int, float)) and isinstance(new_width,(int, float))):
            raise TypeError("Wrong value type")
        self.__lenght, self.__width=new_lenght, new_width

    
    def area(self):
        return self.__width*self.__lenght
        

    def perimeter(self):
        return 2*(self.__width + self.__lenght)
    

    @property
    def lenght(self):
        return self.__lenght


    @property
    def width(self):
        return self.__width
    

    @lenght.setter
    def lenght(self, newlenght):
        if not (newlenght >= 0.0 and newlenght <=20.0) or not isinstance(newlenght, (int, float)):
            raise ValueError("Wrong value")
        self.__lenght = newlenght
            
            
    @width.setter
    def width(self, newwidth):
        if not(newwidth >= 0.0 and newwidth <=20.0) or not isinstance(newwidth, (int, float)):
            raise ValueError("Wrong value")
        self.__width = newwidth
            

x = Rectangle()
print(x.lenght, x.width)
a = Rectangle(25, 15)

print(a.area())
print(a.perimeter())
a.lenght =20.1
a.width=18
print(a.lenght)
print(a.width)

# b= Rectangle(-5, -5)
