# Student Management System
students=[]
# Add student
def add():
    print("=========================================")
    print("---------- ADD STUDENT ----------")
    print("=========================================")
    roll_no = input("Enter Roll No: ")
    
    # Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("This Roll No already exists!")
            return
    
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    semester = input("Enter Semester: ")
    marks = input("Enter Marks: ")
    
    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "semester": semester,
        "marks": marks
        }
    
    students.append(student)
    print("\nStudent added successfully!")
# Delete student
def delete():
    print("=========================================")
    print("---------- DELETE STUDENT ----------")
    print("=========================================")
    roll_no = input("Enter Roll No to Delete: ")
    
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("\n--------------------------------------")
            print("\nStudent deleted successfully!")
            print("\n--------------------------------------")
            return
        print("Student not found!")
# Update student 
def update():
    print("=========================================")
    print("---------- UPDATE STUDENT ----------")
    print("=========================================")
    roll_no=input("Enter the Roll No : ")
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")
            student["semester"] = input("Enter New Semester: ")
            student["marks"] = input("Enter New Marks: ")
            print("\nStudent updated successfully!")
            return
        print("Student not found!")
    
# View student
def view():
    print("=========================================")
    print("---------- VIEW All STUDENT ----------")
    print("=========================================")
    
    if len(students) == 0:
        print("No student data available.")
        return
    
    for student in students:
        print("\n--------------------------------------")
        print(f"\tRoll No    : {student["roll_no"]}")
        print(f"\tName       : {student["name"]}")
        print(f"\tCourse     : {student["course"]}")
        print(f"\tSemester   : {student["semester"]}")
        print(f"\tMarks      : {student["marks"]}")
        print("--------------------------------------")
        
# Search student
def search():
    print("=========================================")
    print("---------- SEARCH STUDENT ----------")
    print("=========================================")
    roll_no=input("Enter the Roll No : ")
    for student in students:
        if student["roll_no"]==roll_no:
            print("---------------------------------------------")
            print(f"\tStudent Roll No : {student["roll_no"]}")
            print(f"\tStudent Name    : {student["name"]}")
            print(f"\tStudent Course  : {student["course"]}")
            print(f"\tStudent Semester: {student["semester"]}")
            print(f"\tStudent Marks   : {student["marks"]}")
            print("---------------------------------------------")
            
            print("\n Student Search Successfully!")
        print("\n Student Not Search!")
def show_heading():
    print("=========================================")
    print("------- STUDENT MANAGEMENT SYSTEM -------")
    print("=========================================")
            
#login interface
print("=======================")
print("\tlogin page")
print("=======================")
username=input("Enter username : ")
password=input("Enter password : ")
if username=="vasu" and password=="12345678":
    print("\nLogin successful!")
    condition=True
    show_heading()
else:
    print("\nWrong Username or Password!")
    condition=False
while condition:
    print("\t============")
    print("\t----MENU----")
    print("\t============")
    print("1. Add Student detail.")
    print("2. Delete Student detail.")
    print("3. Update Student detail.")
    print("4. View Student detail.")
    print("5. Search Student detail.")
    print("6. Exit().\n")
    choice=input("Enter your Choice : ")
    if choice=="1":
        add()
    elif choice=="2":
        delete()
    elif choice=="3":
        update()
    elif choice=="4":
        view()
    elif choice=="5":
        search()
    elif choice=="6":
        print("\nThank you for using Student Management System!")
        break
    else:
        print("\nInvalid Choice! ")
        break
