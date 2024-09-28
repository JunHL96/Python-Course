
#if-else statements
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall): #not negates whatever is in the ( )
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male, but are tall")
else:
    print("You are either not male and not tall")


#if statements and comparisons
def max_num(num1, num2, num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#We can compare booleans, numbers, and strings
#other comparison operators are like <= != == < >
print(max_num(300, 40, 5))