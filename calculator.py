# Ask user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask user to enter the second number
num2 = float(input("Enter the second number: "))

# Show operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get the user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on user's choice
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    # Check if the second number is not zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
