a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def calculator(a, b):
    print(str(a + b) + " is the sum\n")
    print(str(a - b) + " is the difference\n")
    print(str(a * b) + " is the product\n")
    if b != 0:
        print(str(a / b) + " is the division\n")
    else:
        print("Division by zero is undefined\n")

calculator(a, b)
