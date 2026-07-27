import os

def sign_up():
    if os.path.exists("user_info.txt"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        verification = input("Enter An Animal Name To Later Verification: ")

        with open("user_info.txt", "a") as f:
            f.write("%-15s| %-15s| %-15s\n"%(username,password,verification))
    else:
        with open("user_info.txt", "w", encoding="utf-8") as f:
            f.write("%-15s| %-15s| %-15s\n"%("USERNAME", "PASSWORD", "VERIFICATION"))

def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")