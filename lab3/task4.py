try:
    a = str(input("Enter your name: "))
    b = str(input("Enter your cnic: "))
    c = int(input("Enter your age: "))
    d = float(input("Enter your salary: "))
    with open('task4.txt','w') as file:
        file.write(f"Name: {a}\nCNIC: {b}\nAge: {c}\nSalary: {d}\n")
        print("file updated")
        file.close()
    e = str(input("Enter your contact number: "))
    with open('task4.txt', 'a') as file:
        file.write(f"Contact Number: {e}")
        print("file updated")
        file.close()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
