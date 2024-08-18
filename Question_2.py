# Define the list of numbers
numbers = [2, 4, 6, 8, 10]

# Initialize a flag to track if any pair is found
pair_found = False

# Outer loop to iterate through each number in the list
for i in range(len(numbers)):
    # Inner loop to iterate through each number starting from the current index
    for j in range(i, len(numbers)):
        # Check if the sum of the two numbers equals 16
        if numbers[i] + numbers[j] == 16:
            # If a pair is found, display it in the required format
            print(f"Pair found: {numbers[i]} + {numbers[j]}")
            pair_found = True  # Set the flag to True since a pair is found

# If no pair is found, display a message
if not pair_found:
    print("No pair found.")
