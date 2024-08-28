def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 3, 4]
print(f"The product of the numbers in the list is: {multiply(numbers)}")
