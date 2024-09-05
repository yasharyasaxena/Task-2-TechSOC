First I tried using csv but then changed my mind and switched to JSON.
Approach:
  1. Created a flowchart wherein first when you run the program it asks you to choose b/w sign up and log in
  2. then in either of the choices it asks you if you are a student or an admin
  3. If u choose student it checks if u are already registered or not
  4. if not then it asks for your details like first name last name roll no
  5. then it automatically assigns u a user ID combining ur first name and the last 4 digits of roll no
  6. and asks for a password
  7. for admins it asks their name and user-id and checks if the user exists or not and if it doesn't it asks for a password
  8. then in the login part as a student it asks for the user ID and password and checks it if found correct it prints their details as well as marks, CPI, SPI
  9. for admins it asks for the semester and no of courses the admin wants to enter grades for and then using the while loop it repeatedly asks for course code and grade and enters it into another JSON file
  10. after successful entry of this data it asks if the admin wants to log out
  11. it also calculates the spi and cpi after successful entry.
  12. Extensive use of nested dictionaries and loops

Features:
  1. Login and Sign Up
  2. Admin and Student privileges are different.
  3. CPI and SPI calculation
  4. Fixed number of retries for wrong password
  5. 3 files used
  6. Error handling for value errors

Constraint:
  1. The Three JSON files uploaded with code also need to be downloaded for successfully running code.

I could have tried to remove the constraint but I did not have much time left so I just left it.

Only JSON library used
