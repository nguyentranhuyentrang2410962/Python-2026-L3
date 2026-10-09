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
    return courses
def input_marks(students, courses):
    marks = {}
    for course in courses:
        marks[course.course_id] = {}
        print("\nCourse:", course.name)
        for student in students:
            score = float(input(f"Mark for {student.name}: "))
            marks[course.course_id][student.student_id] = score
    return marks