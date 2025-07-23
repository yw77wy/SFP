# Define the function
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

# Test cases
print(calculate(10, "+", 10))  # Output: 20
print(calculate(10, "-", 10))  # Output: 0
print(calculate(10, "*", 10))  # Output: 100
print(calculate(10, "/", 10))  # Output: 1.0
