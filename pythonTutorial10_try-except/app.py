try:
    # This block of code attempts to perform a division by zero, which will raise a ZeroDivisionError
    answer = 10/0
    # The input function asks the user to enter a number and converts the input to an integer.
    # If the user inputs a non-integer, it will raise a ValueError.
    number = int(input("Enter a number: "))
    # If no exceptions are raised, the code will print the entered number.
    print(number)

# This except block catches a ZeroDivisionError (division by zero) if it occurs.
except ZeroDivisionError as err:
    # The error message from the exception is printed.
    print(err)

# This except block catches a ValueError (raised if the input can't be converted to an integer).
except ValueError:
    # If a ValueError occurs, it prints an "Invalid input!" message.
    print("Invalid input! ")

# Avoiding broad except clauses helps ensure that only expected errors are handled, making debugging easier.