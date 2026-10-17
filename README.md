# Student Data Organizer

## 1. Project Overview

The **Student Data Organizer** is a simple menu-driven Python application used to manage student records. It allows users to add, display, update, and delete student information. It also provides a feature to display all the subjects offered by students.

This project is developed using Python programming concepts such as lists, dictionaries, tuples, sets, loops, conditional statements, and string operations.

## 2. Features

The Student Data Organizer provides the following features:

1. **Add Student:** Add a new student record with Student ID, name, age, grade, date of birth, and subjects.
2. **Display All Students:** Display the details of all registered students.
3. **Update Student Information:** Update a student's name, age, grade, or subjects.
4. **Delete Student:** Delete a student record using the Student ID.
5. **Display Subjects Offered:** Display all unique subjects entered for students in alphabetical order.
6. **Exit:** Exit the application.

## 3. Technologies Used

* **Programming Language:** Python
* **Data Structures:** List, Dictionary, Tuple, and Set
* **Concepts Used:** Loops, conditional statements, user input, list comprehension, string methods, and formatted strings.

## 4. Student Information

Each student record contains the following information:

* Student ID
* Name
* Age
* Grade
* Date of Birth
* Subjects
* Student Information Tuple

Student records are stored in a list of dictionaries. Each dictionary contains the details of one student.

## 5. Python Concepts Used

### List

A list stores multiple student records.

```python
students = []
```

### Dictionary

A dictionary stores individual student details using key-value pairs.

```python
student = {
    "id": student_id,
    "name": name,
    "age": age,
    "grade": grade,
    "dob": dob,
    "subjects": b,
    "student_info": student_info
}
```

### Tuple

A tuple stores the student's ID and date of birth together.

```python
student_info = (student_id, dob)
```

### Set

A set stores unique subjects, removing duplicate subject names from the combined collection.

```python
subjects_set = set()
```

### While Loop

The `while True` loop repeatedly displays the menu until the user selects the Exit option.

### Conditional Statements

The `if`, `elif`, and `else` statements execute the appropriate operation based on the user's choice.

### List Comprehension

List comprehension processes the comma-separated subject names and removes unnecessary spaces and empty entries.

## 6. How to Run the Project

Follow these steps to run the application:

1. Install Python on your computer.
2. Open a code editor such as Visual Studio Code or IDLE.
3. Create a Python file named `student_organizer.py`.
4. Copy the project code into the file.
5. Save the file.
6. Open the terminal in the project folder.
7. Run the following command:

```bash
python student_organizer.py
```

8. Select an option from the displayed menu.
9. Follow the instructions to manage student records.

## 7. Main Menu

When the program runs, it displays the following menu:

```text
Welcome to the Student Data Organizer!
Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice:
```

## 8. Example Usage

### Adding a Student

```text
Enter your choice: 1
Enter Student ID: 101
Enter Name: Rahul
Enter Age: 20
Enter Grade: A
Enter Date of Birth (YYYY-MM-DD): 2006-01-15
Enter Subjects (comma-separated): Python, Java, DBMS

Student added successfully!
```

### Displaying Student Records

```text
Enter your choice: 2
--- STUDENT RECORDS ---
ID: 101, Name: Rahul, Age: 20, Grade: A, Date of Birth: 2006-01-15, Subjects: Python, Java, DBMS
```

### Displaying Subjects Offered

```text
Enter your choice: 5
--- SUBJECTS OFFERED ---
DBMS
Java
Python
```

*Note: The example outputs above illustrate typical program usage.*

## 9. Advantages

* Easy to use because of its menu-driven interface.
* Prevents duplicate Student IDs.
* Allows users to update and delete student records.
* Displays subjects without duplicates.
* Demonstrates the practical use of Python data structures.
* Helps beginners understand basic data management operations.

## 10. Limitations

* Student records are stored in memory and are lost when the program terminates.
* The program does not use a database.
* Age input must be a valid integer.
* The program does not perform comprehensive validation of student details.

## 11. Future Improvements

The project can be improved by adding:

* File handling to save student records permanently.
* Database connectivity using SQLite or MySQL.
* Better input validation.
* Search functionality to find students by ID or name.
* Additional student details, such as email address and phone number.
* A graphical user interface.

## 12. Conclusion

The Student Data Organizer is a beginner-friendly Python project that demonstrates how to manage student information using different data structures. It provides basic operations for adding, displaying, updating, and deleting student records, along with displaying unique subjects. This project helps develop practical programming skills and provides a foundation for building more advanced student management systems.

#watch this video
https://drive.google.com/file/d/1TFaqLkGLQSs09QKcrp2QD4yTbDdzHocw/view?usp=sharing
