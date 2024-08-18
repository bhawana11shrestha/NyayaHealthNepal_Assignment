import numpy as np  # Import NumPy package and alias it as 'np'

# Read a space-separated input list of numbers and convert to a list of floats
arr = np.array(input().split(), float)  # Take input, split into list, convert to NumPy array of floats

# Reverse the NumPy array
reversed_arr = arr[::-1]  # Use slicing to reverse the array

# Print the reversed array
print(reversed_arr)  # Output the reversed array
