operation = input("Choose an operation (+, -, *, /): ").strip()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operation == "-":
    num1 -= num2
elif operation == "*":
    num1 *= num2
elif operation == "/":
    if num2 != 0:
         num1 /= num2
    else:
        result = "Error! Division by zero."
elif operation == "+":
    num1 -= (-num2)
else:
    num1 = "Invalid operation selected!"

print(f"Result: {num1}")
