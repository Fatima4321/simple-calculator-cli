'''
    TASK 1
        SIMPLE CALCULATOR
        #1. ADD
        #2. SUBTRACT
        #3. MULTIPLY
        #4. DIVIDE
'''
# Simple Calculator (CLI)

print("Simple Calculator")

try:
    # Taking user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Performing calculations
    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid operator entered.")

except ValueError:
    print("Error: Please enter valid numeric values.")
    