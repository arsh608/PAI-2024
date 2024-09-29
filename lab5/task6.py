class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0

    def display_employee_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def calculate_bonus(self):
        return 0.20 * self.salary

    def hire(self):
        print(f"{self.name} (Manager) is hiring someone.")

class Developer(Employee):
    def calculate_bonus(self):
        return 0.10 * self.salary

    def write_code(self):
        print(f"{self.name} (Developer) is writing code.")

class SeniorManager(Manager):
    def calculate_bonus(self):
        return 0.30 * self.salary

    def hire(self):
        print(f"{self.name} (Senior Manager) is hiring for a senior position.")


manager = Manager("Ali", 100000)
developer = Developer("Baber", 80000)
senior_manager = SeniorManager("Chann", 120000)

manager.display_employee_info()
print(f"Manager's Bonus: ${manager.calculate_bonus()}")
manager.hire()

developer.display_employee_info()
print(f"Developer's Bonus: ${developer.calculate_bonus()}")
developer.write_code()

senior_manager.display_employee_info()
print(f"Senior Manager's Bonus: ${senior_manager.calculate_bonus()}")
senior_manager.hire()
