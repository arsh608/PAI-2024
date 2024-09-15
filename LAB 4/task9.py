#include <iostream>
using namespace std;

class Student {
protected:
    int id;
    string name;

public:
    void setStudentDetails(int student_id, string student_name) {
        id = student_id;
        name = student_name;
    }

    void displayStudentDetails() {
        cout << "Student ID: " << id << endl;
        cout << "Student Name: " << name << endl;
    }
};

class Marks : public Student {
protected:
    int marks_algo;
    int marks_dataScience;
    int marks_calculus;

public:
    void setMarks(int algo, int ds, int calc) {
        marks_algo = algo;
        marks_dataScience = ds;
        marks_calculus = calc;
    }

    void displayMarks() {
        cout << "Marks in Algorithms: " << marks_algo << endl;
        cout << "Marks in Data Science: " << marks_dataScience << endl;
        cout << "Marks in Calculus: " << marks_calculus << endl;
    }
};

class Result : public Marks {
public:
    void displayResult() {
        int total = marks_algo + marks_dataScience + marks_calculus;
        double average = total / 3.0;

        cout << "Total Marks: " << total << endl;
        cout << "Average Marks: " << average << endl;
    }
};

int main() {
    Result student1;

    student1.setStudentDetails(101, "John Doe");
    student1.setMarks(85, 90, 80);

    student1.displayStudentDetails();
    student1.displayMarks();
    student1.displayResult();

    return 0;
}
