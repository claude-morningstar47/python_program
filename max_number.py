# Define a function that takes a list of numbers as input
# and returns the maximum number
def get_max_number(numbers):
    # Initialize a variable to hold the maximum number
    max_number = numbers[0]
    
    # Loop through the list of numbers
    for number in numbers:
        # If the current number is greater than the current maximum number,
        # update the maximum number
        if number > max_number:
            max_number = number
    
    # Return the maximum number
    return max_number

# Test the function with some numbers
print(get_max_number([1, 2, 3, 4, 5]))  # should print 5
print(get_max_number([100, 200, 300, 400, 500]))  # should print 500
print(get_max_number([-1, -2, -3, -4, -5]))  # should print -1
