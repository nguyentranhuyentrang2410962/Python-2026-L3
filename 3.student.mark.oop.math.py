import math
import numpy as np
import curses
students = []
courses = []
marks = {}
def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        print("\nStudent", i + 1)
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")
        student = (student_id, name, dob)
        students.append(student)
    print("\nStudents added successfully.")
def input_courses():
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print("\nCourse", i + 1)
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        credit = int(input("Credit: "))
        course = (course_id, course_name, credit)
        courses.append(course)
    print("\nCourses added successfully.")
def list_students():
    print("\n=== STUDENTS ===")
    for student in students:
        print(student[0], student[1], student[2])
    input("\nPress Enter...")
def list_courses():
    print("\n=== COURSES ===")
    for course in courses:
        print(course[0], course[1], "Credit:", course[2])
    input("\nPress Enter...")
def input_marks():
    for course in courses:
        course_id = course[0]
        marks[course_id] = {}
        print("\nCourse:", course[1])
        for student in students:
            score = float(input(f"Mark for {student[1]}: "))
            marks[course_id][student[0]] = score
    print("\nAll marks saved.")
def show_marks():
    course_id = input("\nEnter course ID: ")
    if course_id not in marks:
        print("No marks for this course.")
        return
    print("\nMarks:")
    for student in students:
        student_id = student[0]
        if student_id in marks[course_id]:
            print(student[1], marks[course_id][student_id])
    input("\nPress Enter...")
def calculate_gpa(student_id):
    total_score = 0
    total_credit = 0
    for course in courses:
        course_id = course[0]
        credit = course[2]
        if course_id in marks:
            if student_id in marks[course_id]:
                mark = marks[course_id][student_id]
                total_score += mark * credit
                total_credit += credit
    if total_credit == 0:
        return 0
    return total_score / total_credit
def show_gpa():
    print("\n=== GPA ===")
    for student in students:
        gpa = calculate_gpa(student[0])
        print(student[1], round(gpa, 2))
    input("\nPress Enter...")
def show_numpy_marks():
    course_id = input("\nEnter course ID: ")
    if course_id not in marks:
        print("No marks.")
        return
    arr = np.array(list(marks[course_id].values()))
    print("\nNumpy Array:")
    print(arr)
    print("Average:", np.mean(arr))
    input("\nPress Enter...")
def sort_students_by_gpa():
    sorted_students = sorted(students, key=lambda student: calculate_gpa(student[0]), reverse=True)
    print("\n=== GPA RANKING ===")
    rank = 1
    for student in sorted_students:
        gpa = calculate_gpa(student[0])
        print(rank, student[1], round(gpa,2))
        rank += 1
    input("\nPress Enter...")
def welcome_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 5, "STUDENT MARK MANAGEMENT SYSTEM")
    stdscr.addstr(2, 5, "Enter to continue...")
    stdscr.refresh()
    stdscr.getch()
input_students()
input_courses()
input_marks()
curses.wrapper(welcome_screen)
while True:
    print("\n=== STUDENT MANAGEMENT === ")
    print("1. List students")
    print("2. List courses")
    print("3. Show marks")
    print("4. Show GPA")
    print("5. GPA Ranking")
    print("6. Numpy Statistics")
    print("7. Exit")
    choice = input("Choose: ")
    if choice == "1":
        list_students()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        show_marks()
    elif choice == "4":
        show_gpa()
    elif choice == "5":
        sort_students_by_gpa()
    elif choice == "6":
        show_numpy_marks()
    elif choice == "7":
        break