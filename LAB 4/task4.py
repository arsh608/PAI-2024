class Employee:
    salary_after_tax=0.0
    def get_data(self):
        self.ename = input("Enter Employee name: ")
        self.salary = float(input("Enter Monthly Salary: "))
        self.tax = float(input("Enter Tax Percentage: "))

    def Salary_after_tax(self):
        tax_amount = (self.tax / 100) * self.salary
        self.salary_after_tax = self.salary - tax_amount

    def update_tax_percentage(self, taxp):
        self.tax = taxp
        print(f"Tax percentage updated to {self.tax}%")

    def display(self):
        print(f"Employee Name: {self.ename}")
        print(f"Salary: {self.salary:.2f}")
        print(f"Salary after tax: {self.salary_after_tax:.2f}")

employee = Employee()
employee.get_data()
employee.Salary_after_tax()
employee.display()

employee.update_tax_percentage(5)
employee.Salary_after_tax()
employee.display()
