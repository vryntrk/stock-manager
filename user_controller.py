import os
import pandas as pd
"""main fonksiyon çağırılacak"""


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
            verification_animal = input("Enter An Animal Name To Later Verification: ")

            with open("user_info.txt", "a") as f:
                f.write(f"{username},{password},{verification_animal}\n")
                print("User Registered Successfully")

            user_database = open(username + "_database.txt", "w")
            user_database.close()
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

        try:
            usernames[0]

        except IndexError:
            print("No User Found")
            print("Redirecting to Sign Up")
            sign_up()
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
                        break
                    else:
                        error_count += 1
                        print("Incorrect Password")
                break

            else:
                error_count += 1
                print("Invalid Username")

        """çağırılan fonksiyon kullanılacak"""

    else:
        print("You Must Create An Account Before Signing In")
        print("Redirecting to Sign Up")
        sign_up()


def verification(dataframe, idx):
    is_verified = False
    while not is_verified:
        verify = input("Enter Your Verification Animal or enter cancel to exit: ")
        if verify == "cancel":
            break
        elif dataframe.loc[idx, "Verification"] == verify:
            is_verified = True
        else:
            print("Incorrect Verification Animal!")
    return is_verified


def edit_user():
    if os.path.exists("user_info.txt"):
        df_user = pd.read_csv("user_info.txt", sep=",", engine="python", header=None, names=["Username", "Password", "Verification"])
        usernames = list(df_user["Username"])

        try:
            usernames[0]

        except IndexError:
            print("No User Found")
            print("Redirecting to Sign Up")
            sign_up()
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
                    new_username = input("Enter New Username or enter cancel to exit: ")
                    if new_username == "cancel":
                        break
                    elif new_username in usernames:
                        print("Username Already Exists!")
                        continue

                    if verification(df_user, index):
                        df_user.loc[index,"Username"] = new_username
                        os.rename(former_username + "_database.txt", new_username + "_database.txt")
                        print("Username Successfully Changed.")
                        break
                df_user.to_csv("user_info.txt", sep=",", header=False, index=False)
                break

            elif option == 2:
                while True:
                    new_password = input("Enter New Password or enter cancel to exit: ")
                    if new_password == "cancel":
                        break
                    if verification(df_user, index):
                        df_user.loc[index,"Password"] = new_password
                        print("Password Successfully Changed.")
                        break
                df_user.to_csv("user_info.txt", sep=",", header=False, index=False)
                break

            elif option == 3:
                while True:
                    new_username = input("Enter New Username or enter cancel to exit: ")
                    if new_username == "cancel":
                        break
                    elif new_username in usernames:
                        print("Username Already Exists!")
                        continue

                    new_password = input("Enter New Password or enter cancel to exit: ")
                    if new_password == "cancel":
                        break

                    if verification(df_user, index):
                        df_user.loc[index, ["Username", "Password"]] = [new_username, new_password]
                        os.rename(former_username + "_database.txt", new_username + "_database.txt")
                        print("Username And Password Successfully Changed.")
                        break
                df_user.to_csv("user_info.txt", sep=",", header=False, index=False)
                break

            elif option == 4:
                break

            else:
                print("Invalid Option")

    else:
        print("You Must Create An Account Before Editing User")
        print("Redirecting to Sign Up")
        sign_up()


def menu():
    print("--- WELCOME ---")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Edit User")
    print("4. Exit")
    return input("Enter your choice (1-4): ")


def user_controller():
    while True:
        choice = menu()
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            edit_user()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Option")


if __name__ == "__main__":
    user_controller()
