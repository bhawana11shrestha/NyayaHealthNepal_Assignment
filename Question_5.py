def mutate_string(string, position, character):
    # Create a new string by slicing and replacing the character at the specified position
    mutated_string = string[:position] + character + string[position + 1:]
    return mutated_string  # Return the modified string


    # Sample input
s = 'abracadabra'
position = 5
character = 'k'

# Call the function and print the result
print(mutate_string(s, position, character))  # Output: 'abrackdabra'