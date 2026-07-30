def add(username):
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
