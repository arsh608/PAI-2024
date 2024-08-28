#----------------------task1---------------------------------------------------
def print_greeting():
    print("Welcome to the application! We're glad to have you here.")

print_greeting()

#----------------------task2---------------------------------------------------
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

#----------------------task3---------------------------------------------------
def calculate_area(length, width):
    area = length * width
    return area

#----------------------task4---------------------------------------------------
def find_maximum(*numbers):
    return max(numbers)

a= find_maximum(90,700,5000,2)
print(a)

#----------------------task5---------------------------------------------------
def show_info(**details):
    for key, value in details.items():
        print(key, ":", value)

show_info(name="Arsh", age=20, occupation="Engineer")

#----------------------task6---------------------------------------------------
rep= input("your good name! ")
print("Hello!", rep)
per=input("I hope you are fine,let me know how I can help you! ")
per= per.upper()

if per=="YES":
    a=input("share your problem with us ")
    print("Thanks for your feedback, we will resolve your problem ")

elif per=="NO":
    print("Thanks for your cooperation ")

else:
    b="Okay! Good to see you , stay connected"
    print(b.center(50))

