def calculate(expression):
    return eval(expression)

calculation = input("Enter a mathematical expression: ")
result = calculate(calculation)
print(f"The result of the calculation is: {result}")