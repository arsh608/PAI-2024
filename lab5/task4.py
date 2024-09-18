class Student:
    def __init__(self, id, name):
        self.student_id = id
        self.name = name

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")


class Marks(Student):
    def __init__(self, id, name, algo, ds, cal):
        super().__init__(id, name)
        self.marks_algo = algo
        self.marks_dataScience = ds
        self.marks_calculus = cal

    def display_marks(self):
        print(f"Marks in Algorithm: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")


class Result(Marks):
    def __init__(self, id, name, algo, ds, cal):
        super().__init__(id, name, algo, ds, cal)

    def calculate_total_and_average(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        return total_marks, average_marks

    def display_results(self):
        total_marks, average_marks = self.calculate_total_and_average()
        self.display_info()
        self.display_marks()
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")

student1 = Result("S12345", "Alice", 85, 90, 78)
student1.display_results()
