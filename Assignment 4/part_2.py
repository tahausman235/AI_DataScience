records = []

# -------------------------------------------------
def add_student():
    name = input("Enter student name: ")
    roll_no = int(input("Enter student roll no: "))
    course = input("Enter student course: ")
    marks = int(input("Enter student marks: "))

    student = {
        "Name": name,
        "Roll no": roll_no,
        "Course": course,
        "Marks": marks
    }
    records.append(student)
    print("Student added successfully...")

# -------------------------------------------------
def display_records():
    if records:
        print("Student Records")
        print("----------------")
        for stud in records:
            print(f"Name: {stud['Name']}")
            print(f"Roll no: {stud['Roll no']}")
            print(f"Course: {stud['Course']}")
            print(f"Marks: {stud['Marks']}")
            print("----------------")
    else:
        print("No records found!")

# -------------------------------------------------
def search_student():
    if records:
        roll_no = int(input("Enter Roll no to search: "))
        for idx, stud in enumerate(records):
            if roll_no == stud["Roll no"]:
                return idx, stud
        return None, None
    else:
        print("No records found!")
        return None, None

# -------------------------------------------------
def update_marks():
    idx, found = search_student()
    if found is not None:
        print("------- RECORD FOUND ---------")
        print(f"Name: {found['Name']}")
        print(f"Roll No: {found['Roll no']}")
        print(f"Course: {found['Course']}")
        print(f"Marks: {found['Marks']}")

        update = int(input("Enter Updated marks: "))
        records[idx]["Marks"] = update
        print("Marks updated successfully!")
        print("------------------------")
    else:
        print("Record not found")

# -------------------------------------------------
def delete_records():
    idx, found = search_student()
    if found is not None:
        records.pop(idx)
        print("Deleted record successfully!")
    else:
        print("Record not found! Unable to delete.")

# -------------------------------------------------
def sort_records():
    if records:
        records.sort(key=lambda x: x["Marks"], reverse=True)
        print("Records sorted by Marks.")
    else:
        print("No records found!")

# -------------------------------------------------
while True:
    print("\n----- Student Records Management System -----")
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Search Student Record")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Sort Records by Marks")
    print("7. Exit")
    print("---------------------------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_records()
    elif choice == 3:
        idx, stud = search_student()
        if stud is not None:
            print("--- Student Found ---")
            print(f"Name: {stud['Name']}")
            print(f"Roll no: {stud['Roll no']}")
            print(f"Course: {stud['Course']}")
            print(f"Marks: {stud['Marks']}")
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
        print("Exiting program...")
        break
    else:
        print("Invalid Choice!!!")
