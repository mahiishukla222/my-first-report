students = []

while True:
    print("Welcome to the Student Data Organizer!")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        student_id = input("Enter Student ID: ")

        if any(s["id"] == student_id for s in students):
            print("Student ID already exists!")
            continue

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        subjects = input("Enter Subjects (comma-separated): ")

        b = [subject.strip() for subject in subjects.split(",")
             if subject.strip()]

        student_info = (student_id, dob)

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": b,
            "student_info": student_info
        }

        students.append(student)

        print("Student added successfully!")

   
    elif choice == "2":

        if not students:
            print("No student records available.")

        else:
            print("--- STUDENT RECORDS ---")

            for student in students:
                print(
                    f"ID: {student['id']}, "
                    f"Name: {student['name']}, "
                    f"Age: {student['age']}, "
                    f"Grade: {student['grade']}, "
                    f"Date of Birth: {student['dob']}, "
                    f"Subjects: {', '.join(student['subjects'])}"
                )

    
    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        for student in students:
            if student["id"] == student_id:

                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Grade")
                print("4. Update Subjects")

                option = input("Enter your choice: ")

                if option == "1":
                    student["name"] = input("Enter New Name: ")

                elif option == "2":
                    student["age"] = int(input("Enter New Age: "))

                elif option == "3":
                    student["grade"] = input("Enter New Grade: ")

                elif option == "4":
                    subjects = input(
                        "Enter New Subjects (comma-separated): "
                    )

                    student["subjects"] = [
                        s.strip() for s in subjects.split(",")
                        if s.strip()
                    ]

                else:
                    print("Invalid choice!")
                    break

                print("Student information updated!")
                break

        else:
            print("Student not found!")

  
    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        for student in students:
            if student["id"] == student_id:
                del students[students.index(student)]
                print("Student deleted successfully!")
                break

        else:
            print("Student not found!")

    elif choice == "5":
        subjects_set = set()

        for student in students:
            subjects_set.update(student["subjects"])

        if subjects_set:
            print("--- SUBJECTS OFFERED ---")

            for subject in sorted(subjects_set):
                print(subject)

        else:
            print("No subjects available.")

   
    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please select from 1 to 6.")