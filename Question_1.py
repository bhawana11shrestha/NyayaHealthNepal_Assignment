import math  # Import the math module for mathematical operations

def calculate_factorial(n):  # Recursive function to calculate factorial
    if n <= 1:  # Base case: if n is 0 or 1, return 1
        return 1
    print(f"Intermediate step: {n} * {n-1}!")  # Display intermediate multiplication step
    return n * calculate_factorial(n - 1)  # Recursive call

def is_perfect_square(num):  # Function to check if a number is a perfect square
    root = math.isqrt(num)  # Calculate integer square root
    return root * root == num  # Check if square of root equals the number

def main():  # Main function to run the program
    while True:  # Loop to get valid input
        try:
            n = int(input("Enter a positive integer: "))  # Get input and convert to integer
            if n < 0:  # Check if input is negative
                print("Please enter a positive integer.")  # Error for negative input
                continue  # Restart the loop
            break  # Exit loop on valid input
        except ValueError:  # Handle non-numeric input
            print("Invalid input. Please enter a valid integer.")  # Error for invalid input

    factorial = calculate_factorial(n)  # Calculate factorial
    print(f"Factorial of {n} is {factorial}")  # Display factorial

    if is_perfect_square(factorial):  # Check if the factorial is a perfect square
        print(f"The factorial of {n} is a perfect square.")  # Output if it is a perfect square
    else:
        print(f"The factorial of {n} is not a perfect square.")  # Output if not

if __name__ == "__main__":  # Standard entry point in Python
    main()  # Run the main function
