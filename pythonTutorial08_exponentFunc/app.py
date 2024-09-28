# This function raises 'baseNum' to the power of 'powNum'
def raiseToPower(baseNum, powNum):
    # Initialize 'result' to 1 (any number raised to the power of 0 is 1)
    result = 1

    # This 'for' loop will repeat 'powNum' times
    # The variable 'index' will take values from 0 to powNum-1, but it is not used in this loop
    for index in range(powNum):  # The loop runs 'powNum' times
        result = result * baseNum  # Multiply 'result' by 'baseNum' in each iteration

    # After the loop finishes, 'result' contains 'baseNum' raised to 'powNum'
    return result