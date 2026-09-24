students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks1 = float(input("Enter Python marks: "))
    marks2 = float(input("Enter Java marks: "))
    marks3 = float(input("Enter SQL marks: "))

    total = marks1 + marks2 + marks3
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "roll_no": roll_no,
        "python": marks1,
        "java": marks2,
        "sql": marks3,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print("Name       :", student["name"])
        print("Roll No    :", student["roll_no"])
        print("Python     :", student["python"])
        print("Java       :", student["java"])
        print("SQL        :", student["sql"])
        print("Total      :", student["total"])
        print("Percentage :", student["percentage"])
        print("Grade      :", student["grade"])


def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll_no"])
            print("Percentage :", student["percentage"])
            print("Grade      :", student["grade"])
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n==============================")
    print(" Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")