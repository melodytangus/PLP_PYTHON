# Simple Calculator Program
print("=== Melody's Simple Calculator ===")
print("Available operations: +, -, *, /")
print()

# Get user inputs
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()
    
    # Perform calculation based on operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Error: Invalid operation! Please use +, -, *, or /")

except ValueError:
    print("Error: Please enter valid numbers!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\nThank you for using Melody's calculator!")