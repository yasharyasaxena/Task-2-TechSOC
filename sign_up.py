import json

def sign_up():
    student = input("\nAre you a student? (Y/N): ").lower()
    if student == 'y':
        first_name = input("\nEnter your First_Name: ").upper()
        last_name = input("\nEnter your Last_Name: ").upper()
        try:
            roll = int(input("\nEnter your Roll Number: "))
        except ValueError:
            print("\nEnter Integer!")
        with open("student_details.json") as f:
            data = json.load(f)
            exists = False
            for user in data.keys():
                if data[user]["Roll_No"] == roll:
                    print("\nAlready registered. Please Login! ")
                    exists = True
            if not exists:
                user_id = first_name + str(roll)[-4:]
                print(f"\nYour User Id is {user_id} ")
                password = input("\nEnter Password: ")

                with open("student_details.json", 'w') as f:
                    data[user_id] ={
                                        "Password":password,
                                        "First_Name":first_name,
                                        "Last_Name":last_name,
                                        "Roll_No":roll
                                        }
                    
                    json.dump(data, f)

                print("\nRegistered! ")
                print("\nNow Log In.")

    elif student == "n":
        first_name = input("\nEnter your First_Name: ").upper()
        last_name = input("\nEnter your Last_Name: ").upper()
        user_id = input("\nEnter your User ID: ")
        with open("admin_details.json") as f:
            data = json.load(f)
            exists = False
            if user_id in data.keys():
                print("\nAlready registered. Please Login! ")
                exists = True
                
            if not exists:
                password = input("\nEnter Password: ")

                with open("admin_details.json", 'w') as f:
                    data[user_id] ={
                                        "Password":password,
                                        "First_Name":first_name,
                                        "Last_Name":last_name,
                                        }
                    
                    json.dump(data, f)

                print("\nRegistered! ")
                print("\nNow Log In.")

