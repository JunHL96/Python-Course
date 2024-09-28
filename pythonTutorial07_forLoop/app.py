for letter in "Giraffe Academy": # for each letter in the string
    print(letter) # print out each letter on every iteration of the loop

friends = ["Jim", "Karen", "Kevin"]

print("printing out each element in the array: ")
for name in friends:
    print(name) # prints out each of the values in the array
len(friends) # prints out the elements in the array

print("using len function to do the same thing: ")
for index in range(len(friends)): # range from 0 to the number of friends in the list
    print(friends[index])

print("setting range using integers")
for index in range(10): # prints out integers based on number of index specified
    print(index)

print("setting a specific beginning and ending range")
for index in range(3, 10): # prints out a range of integers
    print(index)
