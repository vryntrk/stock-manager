import os
import pandas as pd


def sign_up():
    if os.path.exists("user_info.txt"):
        df_user = pd.read_csv("user_info.txt", sep=",", engine="python", header=None, names=["Username", "Password", "Verification"])
        while True:
            username = input("Enter Username: ")
            usernames = list(df_user["Username"])
            if username in usernames:
                print("Username Already Exists")
                continue
            password = input("Enter Password: ")
            verification = input("Enter An Animal Name To Later Verification: ")

            with open("user_info.txt", "a") as f:
                f.write(f"{username},{password},{verification}\n")
                print("User Registered Successfully")
                break
    else:
        f = open("user_info.txt", "w", encoding="utf-8")
        f.close()
        print("Database File Created")

def sign_in():
    if os.path.exists("user_info.txt"):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
    else:
        sign_up()


sign_up()