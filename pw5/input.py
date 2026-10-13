from domains.student import Student
from domains.course import Course
def input_students():
    students = []
    n = int(input("Number of students: "))
    for i in range(n):
        print("\nStudent", i + 1)
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append(
            Student(student_id, name, dob))
    with open("students.txt", "w", encoding = "utf-8") as file:
        for student in students:
            file.write(f"{student.student_id}, {student.name}, {student.dob}\n")
    return students
def input_courses():
    courses = []
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print("\nCourse", i + 1)
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Credit: "))
        courses.append(Course(course_id, name, credit))
    with open("courses.txt", "w", encoding = "utf-8") as file:
        for course in courses:
            file.write(f"{course.course_id}, {course.name}, {course.credit}\n")
    return courses
def input_marks(students, courses):
    marks = {}
    for course in courses:
        marks[course.course_id] = {}
        print("\nCourse:", course.name)
        for student in students:
            score = float(input(f"Mark for {student.name}: "))
            marks[course.course_id][student.student_id] = score
    with open("mark.txt", "w", encoding = "utf-8") as file:
        for course in courses:
            course_id = course.course_id
            for student in students:
                if student.student_id in marks[course_id]:
                    score = marks[course_id][student.student_id]
                    file.write(f"{course_id}, {student.student_id}, {score}\n")
    return marks