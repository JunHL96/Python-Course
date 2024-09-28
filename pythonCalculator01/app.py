from math import *

#Failed Attempt at Adding Two Numbers
'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result) #result will end up adding two strings
'''

'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)
'''

num1 = float(input("Enter a number: ")) #this will auto-convert any user input to a float
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator!")




