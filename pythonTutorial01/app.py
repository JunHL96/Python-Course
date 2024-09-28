
#Setup & Hello World
'''
print("Hello World")
'''


#Drawing a Shape
'''
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
'''

#Variables and Data Types
'''
character_name = "John" #string
character_age = 50 #int
isMale = True #boolean

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
'''

#Working with Strings
'''
phrase = "Giraffe Academy"
print("\"Quotations\"") #backslash is an escape character inside strings, allowing for special characters
print(phrase + " is cool!")
print(phrase.lower()) #converts to lower case
print(phrase.upper()) #converts to upper case
print(phrase.upper().isupper()) #returns boolean
print(len(phrase)) #length function
print(phrase[3]) #specifies index of a string
print(phrase.index("a")) #passes a parameter and returns index
print(phrase.index("Acad")) #passes a parameter and returns index, error if not found
print(phrase.replace("Giraffe", "Elephant")) #replacing part of a string w/ a string
'''

#Working with Numbers
'''
print(-2.0987)
print(3 * 4 + 4.5)
print(10 % 3) #remainder
print(max(4, 6))
print(min(4, 6))

my_num = 5
print(str(my_num) + " is my favorite number") #prints an integer as a string

my_num2 = -5
print(abs(my_num2))
print(pow(my_num2, 2))

print(round(3.2))
print(round(3.7))

from math import * #imports a lot of math functions
print(floor(3.7)) #floor just chops off anything after decimal
print(ceil(3.7)) #always rounds up
print(sqrt(36))
'''

#Getting Input From Users
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age " years old.")





