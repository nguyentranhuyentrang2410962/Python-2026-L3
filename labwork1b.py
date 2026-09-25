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
        course = (course_id, course_name)
        courses.append(course)
    print("\nCourses added successfully.")
def list_students():
    print("\n=== STUDENTS ===")
    for student in students:
        print(
            student[0],
            student[1],
            student[2]
        )
def list_courses():
    print("\n=== COURSES ===")
    for course in courses:
        print(
            course[0],
            course[1]
        )
def input_marks():
    list_courses()
    course_id = input("\nEnter course ID: ")
    if course_id not in marks:
        marks[course_id] = {}
    for student in students:
        score = float(
            input(
                f"Mark for {student[1]}: "
            )
        )
        marks[course_id][student[0]] = score
    print("Marks saved.")
def show_marks():
    course_id = input(
        "\nEnter course ID: "
    )
    if course_id not in marks:
        print("No marks for this course.")
        return
    print("\nMarks:")
    for student in students:
        student_id = student[0]
        if student_id in marks[course_id]:
            print(
                student[1],
                marks[course_id][student_id]
            )
input_students()
input_courses()
while True:
    print("\n===== MENU =====")
    print("1. List students")
    print("2. List courses")
    print("3. Input marks")
    print("4. Show marks")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        list_students()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break