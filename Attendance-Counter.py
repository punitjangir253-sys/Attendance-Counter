# Attendance Counter

total_students = int(input("Enter number of students: "))

present = 0
absent = 0

for i in range(1, total_students + 1):
    attendance = input(f"Student {i} - Present (P) or Absent (A): ").upper()

    if attendance == "P":
        present += 1
    elif attendance == "A":
        absent += 1
    else:
        print("Invalid input! Please enter P or A.")
        # Don't count invalid input
        continue

print("\n----- Attendance Report -----")
print("Total Students:", total_students)
print("Present:", present)
print("Absent:", absent)

attendance_percentage = (present / total_students) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")
