try:
    num1 = int(input('Enter the first number (num1): '))
    num2 = int(input('Enter the second number (num2): '))

    result = num1 / num2
    print(f'Result of {num1} / {num2} is: {result}')

except ValueError:
    print('Error: Please enter valid integer numbers.')
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
