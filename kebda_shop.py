# Welcome to ITI Kebda Shop# Define the initial products and costsproducts = {"kebda": 10, "sogo2": 15, "batates": 5}customer_cart = {}# Define a function to show the current products and costsdef show_products():    print("Our products and costs are:")    for product, cost in products.items():        print(f"{product}: {cost} EGP")# Define a function to add items to the customer's cartdef add_to_cart():    product_name = input("Enter the name of the product you want to buy: ")    if product_name in products:        quantity = int(input("Enter the quantity you want to buy: "))        customer_cart[product_name] = customer_cart.get(product_name, 0) + quantity        print(f"{quantity} {product_name} added to your cart.")    else:        print(f"Sorry, we do not have {product_name} in stock.")# Define a function to print the customer's billdef print_bill():    total_cost = 0    print("Your bill:")    for product, quantity in customer_cart.items():        cost = products[product] * quantity        print(f"{product}: {quantity} x {products[product]} = {cost} EGP")        total_cost += cost    print(f"Total cost: {total_cost} EGP")# Define a function to add a new product to the inventorydef add_product():    product_name = input("Enter the name of the new product: ")    product_cost = int(input("Enter the cost of the new product: "))    products[product_name] = product_cost    print(f"{product_name} added to the inventory with a cost of {product_cost} EGP.")# Define a function to change the cost of an existing productdef change_cost():    product_name = input("Enter the name of the product you want to change the cost of: ")    if product_name in products:        new_cost = int(input("Enter the new cost of the product: "))        products[product_name] = new_cost        print(f"The cost of {product_name} has been changed to {new_cost} EGP.")    else:        print(f"Sorry, we do not have {product_name} in stock.")# Main menu loopwhile True:    print("\nSelect mode:")    print("1. Customer")    print("2. ITI OWNER")    print("0. Exit")    mode = input(">>> ")        if mode == "1":        print("\nCustomer menu:")        print("1. Show products")        print("2. Buy products")        print("3. Print bill")        print("0. Exit")        customer_choice = input("> ")                if customer_choice == "1":            show_products()        elif customer_choice == "2":            add_to_cart()        elif customer_choice == "3":            print_bill()        elif customer_choice == "0":            break        else:            print("Invalid choice.")        elif mode == "2":        print("\nITI OWNER menu:")        print("1. Add new product")        print("2. Show products")        print("3. Add cost")        print("4. Change cost")        print("0. Exit")        owner_choice = input("> ")                if owner_choice == "1":            add_product()        elif owner_choice == "2":            show_products()        elif owner_choice == "3":            product_name = input("Enter the name of the product you want to add cost to: ")            if product_name in products:                additional_cost = int(input("Enter the additional cost: "))                products[product_name] += additional_cost                print(f"{additional_cost} EGP added to the cost of {product_name}.")            else:                print(f"Sorry, we do not have {product_name} in stock.")        elif owner_choice == "4":            change_cost()        elif owner_choice == "0":            break        else:            print("Invalid choice.")        elif mode == "0":        break        else:        print("Invalid choice.")