class Student:
    def __init__(self):
        self._id = None
        self._name = None

    def set_student_details(self, student_id, student_name):
        self.id = student_id
        self.name = student_name

    def display_student_details(self):
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")


class Marks(Student):
    def __init__(self):
        super().__init__()
        self._marks_algo = None
        self._marks_data_science = None
        self._marks_calculus = None

    def set_marks(self, algo, ds, calc):
        self.marks_algo = algo
        self.marks_data_science = ds
        self.marks_calculus = calc

    def display_marks(self):
        print(f"Marks in Algorithms: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_data_science}")
        print(f"Marks in Calculus: {self.marks_calculus}")


class Result(Marks):
    def display_result(self):
        total = self.marks_algo + self.marks_data_science + self.marks_calculus
        average = total / 3.0

        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")


student1 = Result()
student1.set_student_details(101, "John Doe")
student1.set_marks(85, 90, 80)
student1.display_student_details()
student1.display_marks()
student1.display_result()
