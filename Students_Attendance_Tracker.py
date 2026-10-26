# Student Attendance Tracker
# Using Lists and Sets

students = []
present = set()
absent = set()

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ")
    students.append(name)

print("\nMark Attendance (P = Present, A = Absent)")

for name in students:
    status = input(f"{name}: ").upper()

    if status == "P":
        present.add(name)
    elif status == "A":
        absent.add(name)
    else:
        print("Invalid input! Marked as Absent.")
        absent.add(name)

print("\n----- Attendance Report -----")

print("Total Students:", len(students))

print("Present Students:", list(present))
print("Number Present:", len(present))

print("Absent Students:", list(absent))
print("Number Absent:", len(absent))

percentage = (len(present) / len(students)) * 100
print(f"Attendance Percentage: {percentage:.2f}%")
  
