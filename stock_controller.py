import pandas as pd


def add_product(username):
    while True:
        product_category = input("Enter Product Category: ")
        try:
            if not product_category.replace(" ", "").isalpha():
                raise TypeError
            break
        except TypeError:
            print("Product Category Must Contain Only Letters")

    while True:
        product_name = input("Enter Product Name: ")
        try:
            if not product_name.replace(" ", "").isalpha():
                raise TypeError
            break
        except TypeError:
            print("Product Name Must Contain Only Letters")

    while True:
        product_amount = input("Enter Product Amount: ")
        try:
            float(product_amount)
            break
        except ValueError:
            print("Product Amount Must Contain Only Numbers")

    while True:
        product_unit = input("Enter Product Unit: ")
        try:
            if not product_unit.isalpha():
                raise TypeError
            break
        except TypeError:
            print("Product Unit Must Contain Only Letters")

    while True:
        product_cost = input("Enter Product Cost: ")
        try:
            float(product_cost)
            break
        except ValueError:
            print("Product Cost Must Contain Only Numbers")

    while True:
        product_price = input("Enter Product Price: ")
        try:
            float(product_price)
            f = open(username + "_database.txt", "a", encoding="utf-8")
            f.write(f"{product_category.title()},{product_name.title()},{product_amount},{product_unit.upper()},{product_cost},{product_price}\n")
            f.close()
            print("Product Successfully Added.")
            break
        except ValueError:
            print("Product Price Must Contain Only Numbers")


def list_product(username):
    df_stocks = pd.read_csv(username + "_database.txt", sep=",", engine="python", header=None, names=["Category", "Name", "Amount", "Unit", "Cost", "Price"])

    if not df_stocks.empty:
        df_stocks = df_stocks.sort_values(by=["Category"], ascending=True)

        df_stocks = df_stocks.reset_index(drop=True)
        df_stocks.index = df_stocks.index + 1

        print("\nList of Products:")
        print(df_stocks)
    else:
        print("No Products To List")
        print("Redirecting To Add Menu")
        add_product(username)

def edit_product(username):
    df_stocks = pd.read_csv(username + "_database.txt", sep=",", engine="python", header=None, names=["Category", "Name", "Amount", "Unit", "Cost", "Price"])

    if not df_stocks.empty:
        df_stocks = df_stocks.sort_values(by=["Category"], ascending=True)

        df_stocks = df_stocks.reset_index(drop=True)

        df_stocks.index = df_stocks.index + 1

        list_product(username)

        print()

        index_to_edit = 0

        while True:
            try:
                index_to_edit = int(input("Enter The Index Of The Product Which You Would Like To Edit: ")) - 1
                break
            except ValueError:
                print("Invalid Input, The Index Must Be An Integer")
                continue

        print(df_stocks.iloc[index_to_edit])

        while True:
            print("Choose One To Edit:\n"+
                  "1. Category\n"
                  "2. Name\n"
                  "3. Amount\n"
                  "4. Unit\n"
                  "5. Cost\n"
                  "6. Price\n"
                  "7. Exit\n"
                  "(Enter 1-7)")

            choice = input()

            if choice == "1":
                while True:
                    new_category = input("Enter New Category or cancel to exit: ")

                    if new_category.lower() == "cancel":
                        break

                    try:
                        if not new_category.replace(" ", "").isalpha():
                            raise TypeError

                        df_stocks.iloc[index_to_edit, 0] = new_category
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Category Successfully Changed.")

                        break
                    except TypeError:
                        print("Product Category Must Contain Only Letters")



            elif choice == "2":
                while True:
                    new_name = input("Enter New Name or cancel to exit: ")

                    if new_name == "cancel":
                        break

                    try:
                        if not new_name.replace(" ", "").isalpha():
                            raise TypeError

                        df_stocks.iloc[index_to_edit, 1] = new_name
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Name Successfully Changed.")

                        break
                    except TypeError:
                        print("Product Name Must Contain Only Letters")


            elif choice == "3":
                while True:
                    new_amount = float(input("Enter New Amount or cancel to exit: "))

                    if new_amount == "cancel":
                        break

                    try:
                        float(new_amount)

                        df_stocks.iloc[index_to_edit, 2] = new_amount
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Amount Successfully Changed.")
                        break

                    except ValueError:
                        print("Product Amount Must Contain Only Numbers")


            elif choice == "4":
                while True:
                    new_unit = input("Enter New Unit or cancel to exit: ")

                    if new_unit == "cancel":
                        break

                    try:
                        if not new_unit.isalpha():
                            raise TypeError

                        df_stocks.iloc[index_to_edit, 3] = new_unit
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Unit Successfully Changed.")
                        break

                    except TypeError:
                        print("Product Unit Must Contain Only Letters")


            elif choice == "5":
                while True:
                    new_cost = float(input("Enter New Cost or cancel to exit: "))

                    if new_cost == "cancel":
                        break

                    try:
                        float(new_cost)

                        df_stocks.iloc[index_to_edit, 4] = new_cost
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Cost Successfully Changed.")
                        break

                    except ValueError:
                        print("Product Cost Must Contain Only Numbers")


            elif choice == "6":
                while True:
                    new_price = float(input("Enter New Price or cancel to exit: "))

                    if new_price == "cancel":
                        break

                    try:
                        float(new_price)

                        df_stocks.iloc[index_to_edit, 5] = new_price
                        df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)

                        print("Price Successfully Changed.")
                        break

                    except ValueError:
                        print("Product Price Must Contain Only Numbers")


            elif choice == "7":
                break

            else:
                print("Invalid Choice")

    else:
        print("No Products To Edit")
        print("Redirecting To Add Menu")
        add_product(username)


def remove_product(username):
    df_stocks = pd.read_csv(username + "_database.txt", sep=",", engine="python", header=None, names=["Category", "Name", "Amount", "Unit", "Cost", "Price"])

    if not df_stocks.empty:
        df_stocks = df_stocks.sort_values(by=["Category"], ascending=True)
        df_stocks = df_stocks.reset_index(drop=True)

        list_product(username)

        print()

        while True:
            try:
                index_to_remove = int(input("Enter The Index Of The Product Which You Would Like To Remove: ")) - 1
            except ValueError:
                print("Invalid Index, The Index Must Be An Integer")
            else:
                break

        print(df_stocks.iloc[index_to_remove])

        while True:
            question = input(f"Would You Like To Remove Product? (Y/N): ")
            if question.title() == "Y":
                df_stocks = df_stocks.drop(index_to_remove)
                df_stocks.to_csv(username + "_database.txt", sep=",", index=False, header=False)
                print("Product Successfully Removed.")
                break

            elif question.title() == "N":
                print("Operation Cancelled")
                break

            else:
                print("Invalid Option")

    else:
        print("No Products To Remove")
        print("Redirecting To Add Menu")
        add_product(username)


def menu(username):
    print(f"--- HELLO {username} ---")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Remove Product")
    print("4. View All Products")
    print("5. Exit")
    return input("Enter your choice (1-5): ")


def stock_controller(username):
    while True:
        choice = menu(username)
        if choice == "1":
            add_product(username)
        elif choice == "2":
            edit_product(username)
        elif choice == "3":
            remove_product(username)
        elif choice == "4":
            list_product(username)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Option")
