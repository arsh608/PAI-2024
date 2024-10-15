marks = {
    "Physics": int(input("Enter marks of Physics: ")),
    "Chemistry": int(input("Enter marks of Chemistry: ")),
    "Maths": int(input("Enter marks of Maths: ")) }

avg = sum(marks.values()) / len(marks)

high = max(marks, key=marks.get)

print(f"Average Marks: {avg}")
print(f"Subject with highest marks: {high}")
