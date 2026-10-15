student_records=[]
def add_Student():
    id=int(input("Enter the ID of student: "))
    name=(input("Enter the name: "))
    age=int(input("Enter the age: "))
    marks=(int(input("Enter the marks: ")))
    if(age<=0):
        age=int(input("Age must be not 0 or less than that: "))
    if(marks<0 or marks>100):
        marks=int(input("Marks cant be less then 0 or greater then 100: "))
    student_info={
        "ID": id,
        "Name": name,
        "Age": age,
        "Marks": marks
    }
    student_records.append(student_info)
def view_students():
    print(student_records)

def update_students(idTOupdate):
    for students in student_records:
        if(students["ID"]==idTOupdate):
            students["Name"]=input("Enter the NAME to update: ")
            students["Age"]=int(input("Enter the Age you want to update it to: "))
            students["Marks"]=int(input("Enter the marks that you want to update it to: "))
            break
        else:
            print("wrong id")
            update_students(int(input("Enter the ID of the student you want to update: :")))
def delete_student(idTOdelete):
    for students in student_records:
        if(students["ID"]==idTOdelete):
            student_records.remove(students)
            print("Deletion completed")



exit=True
while(exit):
    print("What you want to do: \n")
    print("1.add student\n")
    print("2.view student\n")
    print("3.update student\n")
    print("4.Delete student_info\n")
    print("5.EXIT")
    option=int(input("Whats your option [1,2,3,4,5]: "))
    if(option==5):
        exit=False
    elif(option==1):
        add_Student()
    elif(option==2):
        view_students()
    elif(option==3):
        update_students(int(input("Enter the ID of the student you want to update: :")))
    elif(option==4):
        delete_student(int(input("Enter the id of student which you want to delete: ")))
    else:
        print("Wrong option Choose again")










