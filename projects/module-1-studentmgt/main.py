students = []

def add_student():
    student = {
        "id":int(input("Enter student id: ")),
        "name":input("Enter name: "),
        "age":int(input("Enter age: ")),
        "course":input("Enter Course: "),
        "marks":float(input("Enter marks: "))
    }
    
    students.append(student)
    
    print("Student added successfully.\n")
    
def view_students():
    if not students:
        print("No students found.\n")    
        return
    
    print("Student List")
    print("-"*60)
    
    for student in students:
        print(
            f"{student['id']}\t"
            f"{student['name']}\t"
            f"{student['age']}\t"
            f"{student['course']}\t"
            f"{student['marks']}"         
        )
    print()
    
def search_student():
    student_id = int(input("Enter student id: "))
    
    for student in students:
        if student["id"]==student_id:
            print("\nStudent found:")
            print(student)
            return
    print("Student not found.\n")
        
def update_student():
    
    student_id = int(input("Enter Student Id to update: "))
    
    for student in students:
        if student["id"]==student_id:
            student["name"] = input("Enter new name")
            student["age"] = input("Enter new age")
            student["course"] = input("Enter new course")
            student["mark"] = input("Enter new mark")
            
            print("Student updated successfully.\n")
            return
        print ("Student not found.\n")
        
def delete_student():
    student_id = int(input("Enter Student Id to delete: "))
    
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            print("Student deleted successfully.\n")
            return
    print ("Student not found.\n")
        
def main():
    while True:
        print("****************  Student Management System ***********************")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
            
        elif choice == "2":
            view_students()
            
        elif choice == "3":
            search_student()
            
        elif choice == "4":
            update_student()
            
        elif choice == "5":
            delete_student()
            
        elif choice == "6":
            print("Thank you for using SMS.")
            break
        
        else:
            print("Invalid choice. Please try again.\n")
            
if __name__ =="__main__":
    main()
    
