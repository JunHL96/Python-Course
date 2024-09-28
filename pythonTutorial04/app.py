'''
def cube(num):
    return num*num*num

result = cube(4)
print(result)
'''

def cube(num):
    return num * num * num

# Take input from the user
num1 = int(input("Enter a number to cube: "))

# Call the function and print the result
result = cube(num1)
print("The cube of " + str(num1) + " is: " + str(result))