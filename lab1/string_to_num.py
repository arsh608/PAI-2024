num = input("Enter numbers separated by space: ")

num_arr = num.split()

number = []
for x in num_arr:
    number.append(int(x))

large = max(number)
print(f"The largest number is: {large}")
