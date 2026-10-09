import curses
def welcome_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 5, "STUDENT MARK MANAGEMENT SYSTEM")
    stdscr.addstr(2, 5,"Enter to continue...")
    stdscr.refresh()
    stdscr.getch()
def show_welcome():
    curses.wrapper(welcome_screen)
def list_students(students):
    print("\n=== STUDENTS ===")
    for student in students:
        print(student.student_id, student.name, student.dob)
    input("\nPress Enter...")
def list_courses(courses):
    print("\n=== COURSES ===")
    for course in courses:
        print(course.course_id, course.name, course.credit)
    input("\nPress Enter...")
def show_marks(students, marks):
    course_id = input("\nEnter course ID: ").strip()
    if course_id not in marks:
        print("No marks.")
        return
    print("\nMarks:")
    for student in students:
        if student.student_id in marks[course_id]:
            print(student.name, marks[course_id][student.student_id])
    input("\nPress Enter...")