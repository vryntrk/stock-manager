import os

def sign_up():
    if os.path.exists("user_info.txt"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        verification = input("Enter An Animal Name To Later Verification: ")

        with open("user_info.txt", "a") as f:
            f.write("%-15s| %-15s| %-15s\n"%(username, password, verification))
            print("User Registered Successfully")
    else:
        with open("user_info.txt", "w", encoding="utf-8") as f:
            f.write("%-15s| %-15s| %-15s\n"%("USERNAME", "PASSWORD", "VERIFICATION"))
            print("Database File Created")

def sign_in():
    if os.path.exists("user_info.txt"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
    else:
        sign_up()