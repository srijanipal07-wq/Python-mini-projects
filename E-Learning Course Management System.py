courses = {}

while True:
    print("\n1. Add Course")
    print("2. View Courses")
    print("3. Enroll Course")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")

        courses[course_id] = [name, []]
        print("Course added successfully!")

    elif choice == "2":
        for course_id, data in courses.items():
            print("Course ID:", course_id)
            print("Course Name:", data[0])
            print("Students:", data[1])

    elif choice == "3":
        course_id = input("Enter course ID: ")

        if course_id in courses:
            student = input("Enter student name: ")
            courses[course_id][1].append(student)
            print("Course enrolled successfully!")
        else:
            print("Course not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")