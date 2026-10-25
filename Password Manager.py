import os
from getpass import getpass

m_prd = "cool"


master_password = input("Enter the Master Password: ")

if master_password != m_prd:
     print("Access denied!")
else:
    print("Access Granted")


def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
 
    found = False
    with open("passwords.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip()
 
            if "|" not in data:
                continue
 
            user, passw = data.split("|", 1)
            print("USER:", user, "|", "PASSWORD:", passw)
            found = True
 
    if not found:
        print("No passwords saved yet.")


def add():
    Name = input("Account Name: ")
    Pwd = input("Password: ")

    if not Name or not Pwd:
        print("Both Fields are Required")
        return


    with open('passwords.txt', 'a') as f:
        f.write(Name + "|" + Pwd + "\n")


while True:
    Prd = input(
        "Would you like to add a new password or view existing ones "
        "(view or add), use q to quit: "
    ).lower()

    if Prd == "q":
        break

    if Prd == "view":
        view()
    elif Prd == "add":
        add()
    else:
        print("Invalid Mode.")
