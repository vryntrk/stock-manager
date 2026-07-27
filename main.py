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
        sign_up()


def sign_in():
    if os.path.exists("user_info.txt"):
        df_user = pd.read_csv("user_info.txt", sep=",", engine="python", header=None, names=["Username", "Password", "Verification"])
        usernames = list(df_user["Username"])
        passwords = list(df_user["Password"])

        error_count = 0

        while error_count < 3:
            username = input("Enter Username: ")
            if username in usernames:
                index = usernames.index(username)
                error_count = 0
                while error_count < 3:
                    password = input("Enter Password: ")
                    if passwords[index] == password:
                        print("Access Granted")
                    error_count += 1
                    print("Incorrect Password")

            else:
                error_count += 1
                print("Invalid Username")

    else:
        sign_up()


def rewrite(dataframe):
    with open("user_info.txt", "w") as f:
        for data in dataframe:
            print(f"{data[0]},{data[1]},{data[2]}\n")


def edit_user():
    df_user = pd.read_csv("user_info.txt", sep=",", engine="python", header=None, names=["Username", "Password", "Verification"])
    usernames = list(df_user["Username"])

    former_username = input("Enter Current Username: ")
    index = usernames.index(former_username)

    while True:
        print("Editing Options:\n"
              "1) Only Username\n"
              "2) Only Password\n"
              "3) Both\n"
              "4) Exit\n"
              "(Enter 1-4)")

        option = int(input())

        if option == 1:
            while True:
                new_username = input("Enter New Username: ")

                if new_username in usernames:
                    print("Username Already Exists!")
                    continue

                df_user.loc[index,"Username"] = new_username
                print("Username Successfully Changed.")
                break

        elif option == 2:
            while True:
                new_password = input("Enter New Password: ")

                df_user.loc[index,"Password"] = new_password
                print("Password Successfully Changed.")
                break

        elif option == 3:
            while True:
                new_username = input("Enter New Username: ")

                if new_username in usernames:
                    print("Username Already Exists!")
                    continue

                new_password = input("Enter New Password: ")

                df_user.loc[index] = [new_username, new_password]

                print("Username And Password Successfully Changed.")
                break

        elif option == 4:
            rewrite(df_user)
            break

        else:
            print("Invalid Option")


edit_user()