def employee(name, salary=10000):
    tax_rate = 0.98
    salary = salary *  tax_rate
    print(f"Employee Name: {name}")
    print(f"Salary after tax: {salary}")

employee("Ali", 5000)
employee("ARSH")
