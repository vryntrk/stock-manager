def add(username):
    product_category = input("Enter Product Category: ")
    product_name = input("Enter Product Name: ")
    product_amount = float(input("Enter Product Amount: "))
    product_unit = input("Enter Product Unit: ")
    product_cost = float(input("Enter Product Cost: "))
    product_price = float(input("Enter Product Price: "))

    f = open(username + "_database.txt", "a", encoding="utf-8")
    f.write(f"{product_category.title()},{product_name.title()},{product_amount},{product_unit.upper()},{product_cost},{product_price}\n")
    f.close()
    print("Product Successfully Added.")
