marks=[]

while True:
    print("\n_____Student Marks Management System_____")
    print("1. Insert Marks")
    print("2. Display Marks")
    print("3. Update Marks")
    print("4. Delete Marks")
    print("5. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        mark=int(input("Enter Student Marks: "))
        marks.append(mark)
        print("Marks inserted successfully.")

    elif choice==2:
        if len(marks)==0:
            print("No marks available")

        else:
            print("Students Marks: ")

            for i in range(len(marks)):
                print("Student", i+1, ":" , marks[i])

    elif choice==3:
        student=int(input("Enter Student No. to Update: "))
        if 1<=student<=len(marks):
            new_mark=int(input("Enter New Marks: "))
            marks[student-1]= new_mark
            print("Marks Updated Successfully.")

        else:
            print("Invalid Student No.")

    elif choice==4:
        student=int(input("Enter Student No. to Delete: "))
        if 1<=student<=len(marks):
            marks.pop(student-1)
            print("Marks Deleted Successfully.")

        else:
            print("Invalid Student No.")

    elif choice==5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
