"""Description: This project involves working with fractions. How do you add 1⁄3 + 1⁄5? Create a program that first asks the user which operation they want to do: add, subtract, multiply or divide and then asks for 1, 2 or more fractions to work with. 
The program prints out the result."""
"""In this project I opted for the built in fractions module. At first I attempted to write my own class for the solving but when I stumbled across this module I could hear the bells going off 'work smarter, not harder'. So I did."""

from fractions import Fraction

operator = raw_input('Enter operator as +-* or / ')
fraction1 = raw_input('Fraction 1: ').split(',')
fraction2 = raw_input('Fraction 2: ').split(',')

a = Fraction(int(fraction1[0]), int(fraction1[1]))
b = Fraction(int(fraction2[0]), int(fraction2[1]))

if operator == '*':
	print a * b
elif operator == '-':
	print a - b
elif operator == '+':
	print a + b
else:
	print a / b