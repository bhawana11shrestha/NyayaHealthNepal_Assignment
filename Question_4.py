def sum_of_numbers(input_string):  # Define the function that takes the input string
    # Remove the curly braces and whitespace, then split by commas
    numbers = input_string.strip("{}").split(",")  # Extract numbers as strings
    
    # Convert the extracted numbers to integers and sum them up
    total_sum = sum(int(num) for num in numbers)  # Convert each number to an integer and sum them
    
    return total_sum  # Return the sum of the numbers

    
# Example input
input_str = "{6, 2, 15}"

# Call the function and print the result
print(sum_of_numbers(input_str))  # Output: 23