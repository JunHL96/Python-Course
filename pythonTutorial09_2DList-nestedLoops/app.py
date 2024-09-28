# Define a 2D list (list of lists) representing a grid of numbers
numberGrid = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9],  # Row 2
    [0]         # Row 3
]

# Print a specific element from the grid
# Access the element in the 3rd row (index 2) and 2nd column (index 1)
print(numberGrid[2][1])  # This will print the value 8

# Loop through each row in the 2D list
for row in numberGrid:
    # Loop through each element (column) in the current row
    for column in row:
        # Print the current element
        print(column)