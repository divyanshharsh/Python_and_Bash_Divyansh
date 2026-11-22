students = {
    "Rahul": "A",
    "Priya": "B",
    "Amit": "C"
}

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Display all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            grade = input("Enter grade: ").upper()
            students[name] = grade
            print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")

        if name in students:
            grade = input("Enter new grade: ").upper()
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nStudent Grades:")

        if students:
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found.")

    elif choice == "4":
        print("Exiting Student Grade Manager.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")