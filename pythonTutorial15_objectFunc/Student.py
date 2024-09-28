# Define the Student class
class Student:
    # The constructor method that initializes the attributes of the class
    # __init__ is called automatically when a new object is created
    def __init__(self, name, major, gpa):
        # Initialize the name of the student (e.g., "Jim")
        self.name = name
        # Initialize the major or field of study (e.g., "Business")
        self.major = major
        # Initialize the student's GPA (e.g., 3.12)
        self.gpa = gpa


    # Add the __str__ method to return a string representation of the object
    # __str__ is called when we use print() on an object of the class
    def __str__(self):
        # The method returns a formatted string with the student's details
        # This string will be displayed when we print the object
        return f"Student Name: {self.name}, Major: {self.major}, GPA: {self.gpa}"


    def honorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
