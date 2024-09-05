from sign_up import sign_up
from login import login

while True:
    print("""Welcome to IITI Online Grading System
        To Log In enter 1,
        To Sign Up enter 2,
        To Quit enter 3.
        """)
    try:
        a = int(input(""))
    except ValueError:
        print("\nEnter Integer!")
    
    if a == 1:
        login()
    if a == 2:
        sign_up()
    if a == 3:
        break