import json

def login():
    student = input("\nAre you a student? (Y/N): ").lower()
    logged_in = False
    if student == 'y':
        user_id = input("\nEnter User_ID: ")
        f = open("student_details.json")
        data = json.load(f)
        f.close()
        exists = False
        if user_id in data.keys():
            exists = True
        else:
            print("\nUser doesn't exist. Please Sign Up first.")
        if exists:
            x=0
            while x<3 and not logged_in:
                password = input("\nEnter Password: ")
                if data[user_id]["Password"] == password:
                    print("\nLogin Successful.")
                    logged_in = True

                else:
                    print("\nWrong Password! ")
                    x+=1
                    print(f"{3-x} attempts left.")

        if logged_in:
            with open("marks.json") as f:
                marks = json.load(f)
                print(data)
                print(marks)

    elif student == "n":
        user_id = input("\nEnter User_ID: ")
        f = open("admin_details.json")
        data = json.load(f)
        f.close()
        exists = False
        if user_id in data.keys():
            exists = True
        else:
            print("\nUser doesn't exist. Please Sign Up first.")
        if exists:
            password = input("\nEnter Password: ")
            if data[user_id]["Password"] == password:
                print("\nLogin Successful.")
                logged_in = True

        if logged_in:
            f = open("student_details.json")
            stud_data = json.load(f)
            f.close()
            for user in stud_data.keys():
                i = 1
                print(f"{i}. {stud_data[user]["First_Name"]} ---> {stud_data[user]["Roll_No"]}")
                i+=1
            x = True
            while x:
                try:
                    roll = int(input("\nEnter Roll No of student whose grade you want to set: "))
                except ValueError:
                    print("\nEnter Integer!")
                user_id = ""
                exists = False
                for user in stud_data.keys():
                    if stud_data[user]["Roll_No"] == roll:
                        user_id = user
                        exists = True
                if not exists:
                    print("\nEnter correct roll number!")
                if exists:
                    try:
                        sem = int(input("\nEnter semester number: "))
                        n = int(input("\nEnter number of Courses: "))
                    except ValueError:
                        print("\nEnter Integer!")
                    i = 0
                    while i<n:
                        with open("marks.json") as f:
                            marks = json.load(f)
                            course = input("\nEnter Course Code: ").upper()
                            grade = float(input("\nEnter Grade [1-10]: "))
                            try:
                                marks[user_id][f"Sem{sem}"][course] = grade
                            except KeyError:
                                marks[user_id][f"Sem{sem}"] = {
                                    course : grade
                                }
                            print(marks)
                            with open("marks.json", "w") as f:
                                json.dump(marks, f)
                            
                        i+=1
                    with open("marks.json") as f:
                            marks = json.load(f)
                            for user in marks.keys():
                                x = 0
                                total = 0
                                for y in marks[user].keys():
                                    x+=1
                                    i=0
                                    total_grades = 0
                                    for course in marks[user][y].keys():
                                        i+=1
                                        total_grades += marks[user][y][course]
                                    spi = total_grades/i
                                    total+=spi
                                    marks[user_id][f"Sem{sem}"]["SPI"] = spi
                                    with open("marks.json", "w") as f:
                                        json.dump(marks, f)
                                cpi = total/x
                                stud_data[user_id]["CPI"] = cpi
                                with open("student_details.json", "w") as f:
                                    json.dump(stud_data, f)


                    print("""Do you want to exit?
                          To exit enter y.""")
                    a = input("").lower()
                    if a == "y":
                        x = False
