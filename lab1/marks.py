marks = {
    "Sub1": int(input("Enter marks for Subject 1: ")),
    "Sub2": int(input("Enter marks for Subject 2: ")),
    "Sub3": int(input("Enter marks for Subject 3: "))
}

avg = sum(marks.values()) / len(marks)
per = avg

print(f"Average Marks: {avg}")
print(f"Percentage: {per}%")
