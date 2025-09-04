records = []

def add_student():
    name = input("Enter student name:")
    roll_no = int(input("Enter student roll no:"))
    subject = input("Enter student subject: ")
    marks = int(input("Enter student marks:"))
    records.append([name, roll_no, subject, marks])
    print("Student added successfully...")

# -------------------------------------------------

def display_records():
    if records:
        print("Student records")
        print("----------------")
        for record in records:
            print("Name: ",record[0],"\nRoll no: ",record[1],"\nSubject: ",record[2],"\nMarks: ",record[3])
            print("----------------")
    else:
        print("Not found")

# -------------------------------------------------

def search_student():
    if records:
        roll_no = int(input("Enter Roll no: "))
        for idx,stud in enumerate(records):
            if roll_no == stud[1]:
                return idx, stud
        return None, None
    else:
        print("Not Found")
        return None, None

# --------------------------------------------------

def update_marks():
    idx,found = search_student()
    if found is not None:
        print("------- RECORD FOUND ---------")
        print(f"Name: {found[0]}")
        print(f"Roll No: {found[1]}")
        print(f"Subject: {found[2]}")
        print(f"Marks: {found[3]}")

        update = int(input("Enter Updated marks: "))
        records[idx][3] = update
        print("Marks updated successfully!")
        print("------------------------")
    else:
        print("Record not found")

# --------------------------------------------------

def delete_records():
    rem_stud,idx = search_student()
    if rem_stud is not None:
        records.pop(rem_stud)
        print("Deleted Record successfully")
    else:
        print("Record not found! \nUnable to delete")

# ---------------------------------------------------

def sort_records():
    if records:
        records.sort(key=lambda a:a[3], reverse=True)
        print("Sorting successfully !!!")
    else:
        print("Records not found...")
        
 
while True:
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_records()
    elif choice == 3:
        idx,stud = search_student()
        if stud is not None:
            print("---Student found---")
            print(f"Name: {stud[0]}")
            print(f"Roll no: {stud[1]}")
            print(f"Subject: {stud[2]}")
            print(f"Marks: {stud[3]}")
            print("------------------")
        else:
            print("Record not found !!!")
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_records()
    elif choice == 6:
        sort_records()
    elif choice == 7:
        break
    else:
        print("Invalid Choice!!!")
