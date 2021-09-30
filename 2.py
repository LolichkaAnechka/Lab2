# 2. Create a class called Rational for performing arithmetic with fractions. Write a program to test your class. 
# Use integer variables to represent the private data of the class – the numerator and the denominator. 
# Provide a init() method that enables an object of this class to be initialized when it’s declared. 
# The init() should contain default parameter values in case no initializers are provided and should store the fraction in reduced form. 
# For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator. 
# Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.

class Rational:

    def __init__(self, numerator = 1, denominator = 2):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator
            self.__denominator = denominator
        else:
            raise TypeError("Type Error")
    

    def getFraction(self):
        return self.__numerator,'/', self.__denominator 


    def getFloating(self):
        return self.__numerator/self.__denominator


    def add(self, newnum, newdenom):
        self.__numerator = self.__numerator * newdenom + newnum * self.__denominator
        self.__denominator = self.__denominator * newdenom


    def sub(self, newnum, newdenom):
        self.__numerator = self.__numerator * newdenom - newnum * self.__denominator
        self.__denominator = self.__denominator * newdenom


    def mult(self, newnum, newdenom):
        self.__numerator = self.__numerator * newnum
        self.__denominator = self.__denominator * newdenom


    def div(self, newnum, newdenom):
        self.__numerator = self.__numerator * newdenom
        self.__denominator = self.__denominator * newnum


x=Rational(2, 5)

print(x.getFloating())
print(x.getFraction())

x.add(4, 5)

print(x.getFloating())
print(x.getFraction())

x.sub(1, 2)

print(x.getFloating())
print(x.getFraction())