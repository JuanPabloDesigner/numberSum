# Define a function that takes a cell value as input and returns the sum of its single digits
def sum_single_digits(cell_value):
    # Convert the cell value to a string
    cell_string = str(cell_value)

    # Use a list comprehension to extract the single digits from the string and convert them to integers
    digits = [int(char) for char in cell_string if char.isdigit() and int(char) != 0]

    # Calculate the sum of the digits
    digit_sum = sum(digits)

    # Return the sum of the digits
    return digit_sum

# Example usage
cell_value = "123456"
print(sum_single_digits(cell_value)) # Output: 21
