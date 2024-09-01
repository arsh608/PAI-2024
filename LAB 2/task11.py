students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 91],
    "Charlie": [76, 85, 80]
}

def add_grade(student_name, grade):
    if student_name in students_grades:
        students_grades[student_name].append(grade)
        print(f"Added grade {grade} for {student_name}.")
    else:
        print("Student not found.")

def calculate_average(student_name):
    if student_name in students_grades:
        grades = students_grades[student_name]
        average = sum(grades) / len(grades)
        print(f"Average grade for {student_name}: {average:.2f}")
    else:
        print("Student not found.")

def add_student(student_name):
    if student_name not in students_grades:
        students_grades[student_name] = []
        print(f"Added new student: {student_name}")
    else:
        print("Student already exists.")

def remove_student(student_name):
    if student_name in students_grades:
        del students_grades[student_name]
        print(f"Removed student: {student_name}")
    else:
        print("Student not found.")

add_grade("Alice", 95)
calculate_average("Alice")
add_student("David")
remove_student("Charlie")
