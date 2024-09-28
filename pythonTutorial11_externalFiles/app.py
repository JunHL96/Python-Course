'''
employeeFile = open("scratch.txt", "r")

print("Check if file is readable: ")
print(employeeFile.readable())

print("Read the file: ")
print(employeeFile.read())

print("Read a specific line: ")
print(employeeFile.readline())
print(employeeFile.readline())

print("Read all as array: ")
print(employeeFile.readlines())

print("Read a specific index in the array: ")
print(employeeFile.readlines()[1])

employeeFile.close()
'''

# Open the file in read mode ("r")
employeeFile = open("scratch.txt", "r")

# Check if the file is readable (returns True if it is readable)
print("Check if file is readable: ")
print(employeeFile.readable())  # This will print True if the file is readable.

# Read the entire file content and print it.
print("Read the file: ")
print(employeeFile.read())  # Reads the entire file content.

# Reset the file cursor back to the beginning of the file
employeeFile.seek(0)  # Now, the next read operations will start from the beginning.

# Read and print the first two lines of the file
print("Read a specific line: ")
print(employeeFile.readline())  # Reads the first line
print(employeeFile.readline())  # Reads the second line

# Reset the file cursor back to the beginning before reading all lines
employeeFile.seek(0)

# Read all lines into a list (array) and print it.
print("Read all as array: ")
lines = employeeFile.readlines()  # This will read the entire file into a list, where each element is a line.
print(lines)

# Access the second line (index 1) from the array (list) and print it.
print("Read a specific index in the array: ")
if len(lines) > 1:  # Check if there is a second line to prevent an IndexError
    print(lines[1])  # This prints the second line (index 1)
else:
    print("The file doesn't have enough lines.")

# Close the file to release system resources.
employeeFile.close()
