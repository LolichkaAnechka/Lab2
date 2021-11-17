# 2. Create a class called Rational for performing arithmetic with fractions. Write a program to test your class. 
# Use integer variables to represent the private data of the class – the numerator and the denominator. 
# Provide a init() method that enables an object of this class to be initialized when it’s declared. 
# The init() should contain default parameter values in case no initializers are provided and should store the fraction in reduced form. 
# For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator. 
# Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.
from math import gcd

class Rational:
	def __init__(self, numerator, denominator):
		self.__check(numerator, denominator)
		self.__numerator, self.__denominator = self.__reduced_form(numerator, denominator)
		

	def getFraction(self):
		return f'{self.__numerator} / {self.__denominator}' 


	def getFloating(self):
		return self.__numerator/self.__denominator


	def __check(self, numer, denom):
		if not(isinstance(numer, int) and isinstance(denom, int)):
			raise TypeError("Wrong value type")
		if not denom:
			raise ZeroDivisionError("Division by Zero")
		return None


	def add(self, newnum:int, newdenom:int):
		self.__check(newnum, newdenom)
		self.__numerator, self.__denominator = self.__reduced_form(
				self.__numerator * newdenom + newnum * self.__denominator, 
				self.__denominator * newdenom)


	def sub(self, newnum:int, newdenom:int):
		self.__check(newnum, newdenom)
		self.__numerator, self.__denominator = self.__reduced_form(
				self.__numerator * newdenom - newnum * self.__denominator, self.__denominator * newdenom)


	def mult(self, newnum:int, newdenom:int):
		self.__check(newnum, newdenom)
		self.__numerator, self.__denominator = self.__reduced_form(
				self.__numerator * newnum, self.__denominator * newdenom)


	def div(self, newnum:int, newdenom:int):
		self.mult(newdenom, newnum)


	def __reduced_form(self, numer, denom):
		k = gcd(numer, denom)
		return numer//k, denom//k

	

x=Rational(2, 5)

print(x.getFloating())
print(x.getFraction())

x.add(4, 5)

print(x.getFloating())
print(x.getFraction())

x.sub(1, 2)

print(x.getFloating())
print(x.getFraction())

x.div(4, 5)

print(x.getFloating())
print(x.getFraction())

x.sub(1, 0)

print(x.getFloating())
print(x.getFraction())
