#Lists
'''
friends = ["Kevin", "Karen", "Jim", "Ian", "Kevin", "Eugene"]

print(friends[0])
print(friends[1])
print(friends[2])


print("indexing in reverse order")
#Note that for reverse order, it starts at -1 instead of -0 or 0
print(friends[-1])

print("prints the string on the index specified and everything after")
print(friends[3:])

print("specifies a range up to (but not including)")
print(friends[1:3])
'''

#Using functions w/ lists in Python
friends = ["Kevin", "Karen", "Jim", "Jim", "Ian", "Kevin", "Eugene"]
lucky_numbers = [9, 2, 5235, 22, -1, 5, 16]


print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.sort() #prints in alphabetical number
print(friends)
friends.extend(lucky_numbers) #adding one list to another
print(friends)
friends.append("Esther")
print(friends)
friends.pop() #removes last element in the list
print(friends)
friends.index("Kevin") #tells me the index of where Kevin is in the list. Error if not in the list
print(friends.count("Jim"))
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
friends.clear()


