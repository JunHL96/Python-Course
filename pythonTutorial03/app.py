#Tuples - type of data structure. it is a structure where we can store multiple pieces of information.
#tuples are often used in coordinates, are indexed starting at 0 like lists
#Differences w/ lists - tuples are immutable
#Usecases - data that won't change or be modified ever
'''
coordinates = (4, 5)

print(coordinates)
print(coordinates[1])
'''

#Functions in Python
def sayHi():
    #Code that is inside this function MUST be indented
    print("Hello User")

print("Top")
sayHi()
print("Bottom")

#Function with input
def sayHi(name, age):
    print("Hello " + name +", you are " + str(age) + " years old!")

sayHi("Mike", 35)
