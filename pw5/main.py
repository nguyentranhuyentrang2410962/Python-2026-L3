import numpy as np
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_marks
students = input_students()
courses = input_courses()
marks = input_marks(students, courses)
def calculate_gpa(student):
    total_score = 0
    total_credit = 0
    for course in courses:
        course_id = course.course_id
        credit = course.credit
        if course_id in marks:
            if student.student_id in marks[course_id]:
                mark = marks[course_id][student.student_id]
                total_score += mark * credit
                total_credit += credit
    if total_credit == 0:
        return 0
    return total_score / total_credit
def show_gpa():
    print("\n=== GPA ===")
    for student in students:
        gpa = calculate_gpa(student)
        print(student.name, round(gpa, 2))
    input("\nPress Enter...")
def sort_students_by_gpa():
    sorted_students = sorted(students, key=calculate_gpa, reverse=True)
    print("\n=== GPA RANKING ===")
    rank = 1
    for student in sorted_students:
        gpa = calculate_gpa(student)
        print(rank, student.name, round(gpa, 2))
        rank += 1
    input("\nPress Enter...")
def show_numpy_marks():
    course_id = input("\nEnter course ID: ").strip()
    if course_id not in marks:
        print("No marks.")
        input("\nPress Enter...")
        return
    arr = np.array(list(marks[course_id].values()))
    print("\n=== NUMPY STATISTICS ===")
    print(arr)
    print("Average:", round(np.mean(arr), 2))
    input("\nPress Enter...")
while True:
    print("\n=== STUDENT MANAGEMENT ===")
    print("1. List students")
    print("2. List courses")
    print("3. Show marks")
    print("4. Show GPA")
    print("5. GPA Ranking")
    print("6. NumPy Statistics")
    print("7. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        list_students(students)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        show_marks(students, marks)
    elif choice == "4":
        show_gpa()
    elif choice == "5":
        sort_students_by_gpa()
    elif choice == "6":
        show_numpy_marks()
    elif choice == "7":
        break