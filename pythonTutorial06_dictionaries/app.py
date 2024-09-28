# A dictionary is a built-in data type that stores key-value pairs
# dictionary syntax - created using braces {} and each key-value pair are separated by a colon :
from calendar import month

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    0: "October",
    11: "November",
    12: "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Nov"))

# If a key is not mappable to anything, we can set a default value
print(monthConversions.get("Yoo", "Not a valid Key"))
print(monthConversions.get(1, "Not a valid Key"))
