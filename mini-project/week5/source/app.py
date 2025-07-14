import csv


# Print main menu options
def main_menu_opts():
    print(
        "welcome to the main menu, what would you like to do:\n1: Print products Menu,\n2: Print couriers Menu,\n3: Print orders Menu\n0: Exit app"
    )


# Print product menu options
def products_menu_opts():
    print(
        "welcome to the products, what would you like to do: \n 1: View all products, \n 2: Add new products, \n 3: Update existing product, \n 4: Delete a product, \n 0: return to main menu"
    )


# Print orders menu options
def orders_menu_opts():
    print(
        "welcome to the Orders, what would you like to do:\n1: Display Orders,\n2: Create new Order,\n3: Update Order status,\n4: Update Existing Order,\n5: delete an order\n0: return to main menu"
    )


# Print couriers menu options


def couriers_menu_options():
    print(
        "welcome to the couriers, what would you like to do: \n 1: View all couriers\n2: Add new couriers\n3: Update existing courier\n4: Delete a courier\n 0: return to main menu"
    )


# empty variables to hold the imported data from the txt files locally in python
products_data = []

couriers_data = []

orders = []


# open() functions to import and read to empty variables the data from the csv files
def prod_file_open():
    with open("mini-project/week4/data/products.csv") as temp_products_data:
        products_data
        reader = csv.DictReader(temp_products_data)
        temp_dict = {}
        for row in reader:
            temp_dict = dict(Product=row["Product"], Price=row["price"])
            products_data.append({int(row["Index"]): temp_dict})


def courier_file_open():
    with open("mini-project/week4/data/couriers.csv") as temp_couriers_data:
        reader = csv.DictReader(temp_couriers_data)
        temp_dict = {}
        for row in reader:
            temp_dict = dict(Name=row["Name"], Phone=row["Phone"])
            couriers_data.append({int(row["Index"]): temp_dict})


def order_file_open():
    with open("mini-project/week4/data/orders.csv") as temp_orders_data:
        reader = csv.DictReader(temp_orders_data)
        temp_dict = {}
        for row in reader:
            temp_dict = dict(
                customer_name=row["customer_name"],
                customer_address=row["customer_address"],
                customer_phone=str(row["customer_phone"]),
                courier=int(row["courier"]),
                status=row["status"],
                items=row["items"],
            )
            orders.append({int(row["order_num"]): temp_dict})


# function for add new products to the products data file
def add_product():
    global products_data
    new_product = input("what is the new product you would like to add?\n")
    new_prod_price = float(
        input(
            f"what is the price you would like to charge for {new_product}?\ninsert price here (don't forget the decimal point)"
        )
    )
    temp_prod_dict = dict(Product=new_product, Price=new_prod_price)
    products_data.append({len(products_data) + 1: temp_prod_dict})


# data persistance elements for couriers and products


def products_persistance():
    with open(
        "mini-project/week4/data/products.csv", "w"
    ) as temp_updated_products_data:
        fieldnames = ["Index", "Product", "price"]
        writer = csv.DictWriter(temp_updated_products_data, fieldnames=fieldnames)
        writer.writeheader()
        for item in products_data:
            for key, value in item.items():
                index = products_data.index(item) + 1
                writer.writerow(
                    {
                        "Index": index,
                        "Product": value["Product"],
                        "price": value["Price"],
                    }
                )
    products_data.clear()
    prod_file_open()


def couriers_persistance():
    with open(
        "mini-project/week4/data/couriers.csv", "w"
    ) as temp_updated_couriers_data:
        fieldnames = ["Index", "Name", "Phone"]
        writer = csv.DictWriter(temp_updated_couriers_data, fieldnames=fieldnames)
        writer.writeheader()
        for item in couriers_data:
            for key, value in item.items():
                index = couriers_data.index(item) + 1
                writer.writerow(
                    {"Index": index, "Name": value["Name"], "Phone": value["Phone"]}
                )
    couriers_data.clear()
    courier_file_open()



def orders_persistance():
    with open("mini-project/week4/data/orders.csv", "w") as temp_updated_orders_data:
        fieldnames = [
            "order_num",
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        writer = csv.DictWriter(temp_updated_orders_data, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            for key, value in order.items():
                index = orders.index(order) + 1
                writer.writerow(
                    {
                        "order_num": int(index),
                        "customer_name": value["customer_name"],
                        "customer_address": value["customer_address"],
                        "customer_phone": str(value["customer_phone"]),
                        "courier": value["courier"],
                        "status": value["status"],
                        "items": str(value["items"]),
                    }
                )
    orders.clear()
    order_file_open()


# function for creating a new courier


def add_courier():
    global couriers_data
    new_courier = input("what is the new courier you would like to add?\n")
    courier_phone = input(
        f"Enter the number you would like to give to {new_courier}\nEnter new number here (remember the number must start 020 and be 11 digits long) > "
    )
    if courier_phone[0] == "0" and len(courier_phone) == 11:
        print(
            f"\nThe new courier will be named {new_courier} and it's number will be {courier_phone}. Confirmed\n"
        )
        temp_dict = dict(Name=new_courier, Phone=courier_phone)
        couriers_data.append({len(couriers_data) + 1: temp_dict})
    else:
        print("Thats and invalid number, please try again")
        add_courier()


# function for adding a new order


def add_order_func():
    global orders
    global products_data
    global couriers_data
    customername = input("please enter the customers name > ")
    customeraddress = input("please enter the street and city of the customer > ")
    customerphone = input("Please enter the customers phone number > ")
    for item in products_data:
        for key, value in item.items():
            print(f"{key}.{value["Product"]}\n")
    selected_items = []
    selected_item_index = []

    def item_selection():
        itemorderedinput = int(
            input(
                "Please select the item(s) the customer would like to order - (input the number corresponding with the desired item, if order more than one item, enter the first one and wait to be prompted for subsequent item selections > "
            )
        )
        itemorderedinput -= 1
        confirmation_input = int(
            input(
                f"you have selected {products_data[itemorderedinput][itemorderedinput + 1]["Product"]}, How would you like to proceed - \n 1 - add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} to order and confirm item's selection \n 2 - add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} to order and add another item \n 3 - don't add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} and return to the orders menu > "
            )
        )
        if confirmation_input == 1:
            selected_items.append(
                {products_data[itemorderedinput][itemorderedinput + 1]["Product"]}
            )
            print(
                f"Confirmed, the following items have been added to the order {str(selected_items)}"
            )
            selected_item_index.append(str(itemorderedinput + 1))
        elif confirmation_input == 2:
            selected_items.append(
                {products_data[itemorderedinput][itemorderedinput + 1]["Product"]}
            )
            selected_item_index.append(str(itemorderedinput + 1))
            item_selection()
        elif confirmation_input == 3:
            orders_menu_opts
        else:
            print("Thats an invalid response, please try again")
            item_selection()

    item_selection()

    num = 1
    for item in couriers_data:
        for key, value in item.items():
            print(f"{key}.{value["Name"]}\n")
            num += 1
    courier_choice = int(
        input(
            "\nFrom the list above, please select the courier you would like to assign to the order"
        )
    )
    courier_selection = couriers_data[courier_choice - 1][courier_choice]["Name"]
    print(
        f"You have selected {courier_selection} for this order, it will now be assigned"
    )

    new_order = {
        f"{len(orders)+1}": {
            "customer_name": customername,
            "customer_address": customeraddress,
            "customer_phone": customerphone,
            "Courier": courier_selection,
            "status": "preparing",
            "items": selected_items,
        }
    }
    print(
        f"\n This is your new order which has now been added to the orders list >\n {new_order}"
    )
    selected_item_index = str(selected_item_index)
    selected_item_index = selected_item_index.strip("[").strip("]").replace("'", "")
    formated_order = {
        f"{len(orders) + 1}": {
            "customer_name": customername,
            "customer_address": customeraddress,
            "customer_phone": customerphone,
            "courier": courier_choice,
            "status": "preparing",
            "items": f"{selected_item_index}",
        }
    }
    orders.append(formated_order)


# function for updating an existing order status

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]


def update_order_status():
    global orders
    global order_status
    for order in orders:
        for key, value in order.items():
            print(
                f"Order {key}: {value['customer_name']}, Items Order: {value['items']}, Status: {value['status']}"
            )
    print("\n")
    change_selection1 = int(
        input(
            "Which order would like to update the status for? input the number for the associated order > "
        )
    )
    print(
        f"what would you like to change order {change_selection1} to? below is the available options"
    )
    num = 1
    for status in order_status:
        print(f"{num}. {status}")
        num += 1
    change_selection2 = int(
        input(
            f"whats the number associated with the status you would like to update order {change_selection1} to?"
        )
    )

    if change_selection2 <= 4:
        for order_key in orders[change_selection1 - 1].keys():
            orders[change_selection1 - 1][order_key]["status"] = order_status[
                change_selection2 - 1
            ]
    for order in orders:
        for key, value in order.items():
            print(
                f"Order {key}: {value['customer_name']}, Items Order: {value['items']}, Status: {value['status']}"
            )


# function for updating existing order


def update_order():
    global orders
    global products_data
    dict_key_directory = [
        "customer_name",
        "customer_address",
        "customer_phone",
        "status",
        "items",
        "Courier",
    ]
    for order in orders:
        for order_num, order_detail in order.items():
            print(
                f"Order {order_num}: customer name: {order_detail['customer_name']} status: {order_detail['status']} items ordered: {order_detail['items']} Courier: {order_detail['courier']} "
            )
    print("\n")
    change_selection1 = int(
        input(
            "Which order would like to update? input the number for the associated order > "
        )
    )
    change_selection2 = int(
        input(
            "what would you like to change about the order.\n1. customer name\n2. customer address\n3. customer phone number\n4. order status\n5. items ordered\n6. Courier\n> "
        )
    )
    if change_selection2 == 1:
        for key in orders[change_selection1 - 1].keys():
            order_key = key
        change_selection3 = input(
            f"what would you like to change the customer name of {order_num} to? > "
        )
        orders[change_selection1 - 1][change_selection1][
            dict_key_directory[change_selection2 - 1]
        ] = change_selection3
    elif change_selection2 == 2:
        for key in orders[change_selection1 - 1].keys():
            order_key = key
        change_selection4 = input(
            f'what would you like to change the customer address of {order_num} to? *remember the "street, city" format> '
        )
        orders[change_selection1 - 1][order_key][
            dict_key_directory[change_selection2 - 1]
        ] = change_selection4
    elif change_selection2 == 3:
        for key in orders[change_selection1 - 1].keys():
            order_key = key
            change_selection5 = input(
                f"what would you like to change the customer number of {order_num} to? NOTE: number must begin with 0 > "
            )
            if "0" in change_selection5[0] and len(change_selection5) == 11:
                orders[change_selection1 - 1][order_key][
                    dict_key_directory[change_selection2 - 1]
                ] = change_selection5
            else:
                print("\nThats not a valid number please try again")
                update_order()
    elif change_selection2 == 4:
        update_order_status()
    elif change_selection2 == 5:
        order_update_input = int(
            input(
                f"What would you like to do?\n1. Add new item to {order_num}\n2. remove item(s) from {order_num}"
            )
        )
        if order_update_input == 1:
            selected_items = []
            selected_item_index = []

            def add_item():
                for item in products_data:
                    for key, value in item.items():
                        print(f"{key}.{value["Product"]}\n")
                itemorderedinput = int(
                    input(
                        "Please select the item(s) the customer would like to add to the order - (input the number corresponding with the desired item, if order more than one item, enter the first one and wait to be prompted for subsequent item selections > "
                    )
                )
                itemorderedinput -= 1
                confirmation_input = int(
                    input(
                        f"you have selected {products_data[itemorderedinput][itemorderedinput + 1]["Product"]}, How would you like to proceed - \n 1 - add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} to order and confirm item's selection \n 2 - add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} to order and add another item \n 3 - don't add {products_data[itemorderedinput][itemorderedinput + 1]["Product"]} and return to the orders menu > "
                    )
                )
                if confirmation_input == 1:
                    selected_items.append(
                        {
                            products_data[itemorderedinput][itemorderedinput + 1][
                                "Product"
                            ]
                        }
                    )
                    print(
                        f"Confirmed, the following items have been added to the order: {str(selected_items)}"
                    )
                    selected_item_index.append(str(itemorderedinput + 1))
                elif confirmation_input == 2:
                    selected_items.append(
                        {
                            products_data[itemorderedinput][itemorderedinput + 1][
                                "Product"
                            ]
                        }
                    )
                    selected_item_index.append(str(itemorderedinput + 1))
                    add_item()
                elif confirmation_input == 3:
                    orders_menu_opts
                else:
                    print("Thats an invalid response, please try again")
                    add_item()

            add_item()
            selected_item_index = str(selected_item_index)
            selected_item_index = (
                selected_item_index.strip("[").strip("]").replace("'", "")
            )
            orders[change_selection1 - 1][change_selection1][
                "items"
            ] += f", {selected_item_index}"
        elif order_update_input == 2:

            def rmv_order_item():
                order_temp_items = orders[change_selection1 - 1][change_selection1][
                    "items"
                ]
                print(
                    f"Below are the items that order {change_selection1} currently has\n"
                )
                for key, value in orders[change_selection1 - 1].items():
                    rmv_ord_items = value["items"].split(",")
                    for ord_item in rmv_ord_items:
                        ord_item = int(ord_item)
                        print(
                            f'Item {ord_item}: {products_data[ord_item - 1][ord_item]["Product"]}'
                        )

                itemremoveinput = int(
                    input(
                        "Please select the item(s) the customer would like to remove from the order - (input the number corresponding with the desired item, if more than one item, enter the first one and wait to be prompted for subsequent item selections > "
                    )
                )
                confirmation_input = int(
                    input(
                        f"you have selected Item {itemremoveinput}: {products_data[itemremoveinput-1][itemremoveinput]["Product"]}, How would you like to proceed - \n 1 - remove item {itemremoveinput}: {products_data[itemremoveinput-1][itemremoveinput]["Product"]} from order and confirm item's remove \n 2 - remove item {itemremoveinput}: {products_data[itemremoveinput-1][itemremoveinput]["Product"]} from order and remove another item \n 3 - don't remove item {itemremoveinput}: {products_data[itemremoveinput-1][itemremoveinput]["Product"]} and return to the orders menu > "
                    )
                )
                if confirmation_input == 1:
                    items = orders[change_selection1 - 1][change_selection1]["items"]
                    items = items.split(",")
                    items.remove(str(itemremoveinput))
                    items = str(items)
                    items = (
                        items.strip("[")
                        .strip("]")
                        .replace("'", "")
                        .strip()
                        .replace("  ", " ")
                    )
                    orders[change_selection1 - 1][change_selection1]["items"] = items
                elif confirmation_input == 2:
                    orders[change_selection1 - 1][order_key][
                        dict_key_directory[change_selection2 - 1]
                    ].pop(itemremoveinput)
                    rmv_order_item()
                elif confirmation_input == 3:
                    orders_menu_opts()
                else:
                    print("Thats an invalid response, please try again")
                    rmv_order_item()

            rmv_order_item()
    elif change_selection2 == 6:
        for courier in couriers_data:
            for key, value in courier.items():
                print(f"{key}. {value["Name"]}")
        for key in orders[change_selection1 - 1].keys():
            order_key = key
        change_selection3 = int(
            input(
                f"which courier from the ones listed above would you like to change the courier of order {order_num} to?, input the number of the courier below\n> "
            )
        )
        orders[change_selection1 - 1][change_selection1]["courier"] = change_selection3


# function for updating existing product
def prod_update():
    for prod in products_data:
        for index, value in prod.items():
            print(f'{index}. {value["Product"]} - £{value["Price"]}')
    prod_update_input = int(
        input(
            "What is the product you would like to update? please give the number associated with the product\n"
        )
    )
    if prod_update_input <= len(products_data):
        update_choice = int(
            input(
                (
                    f"You selected {products_data[prod_update_input-1][prod_update_input][
            "Product"
        ]}, what would you like to update about it?\n1. Update Product Name\n2.Update Product Price\n"
                )
            )
        )
        if update_choice == 1:
            new_prod_name = input(
                f'Enter the new name you would like to give to {products_data[prod_update_input-1][prod_update_input][
            "Product"
        ]} below\n> '
            )
            print(
                f'The new name for {products_data[prod_update_input-1][prod_update_input][
            "Product"]} will be {new_prod_name}, confirmed\n'
            )
            products_data[prod_update_input - 1][prod_update_input][
                "Product"
            ] = new_prod_name
        elif update_choice == 2:
            new_prod_price = float(
                input(
                    f'Enter the new price you would like to give to {products_data[prod_update_input-1][prod_update_input][
            "Product"]}?\nThe current price is £{products_data[prod_update_input - 1][prod_update_input][
            "Price"]}\nEnter new price here (remember the format 0.00) > '
                )
            )
            print(
                f'The new price for {products_data[prod_update_input-1][prod_update_input][
            "Price"]} will be £{new_prod_price}, confirmed\n'
            )
            products_data[prod_update_input - 1][prod_update_input][
                "Price"
            ] = new_prod_price
        else:
            print("Thats and invalid input, please try again")
            prod_update()
    else:
        print("That's not a valid option please try again\n")
        prod_update()


# function for updating courier information


def courier_update():
    for courier in couriers_data:
        for index, value in courier.items():
            print(f"{index}. {value["Name"]} - {value["Phone"]}")
    cour_update_input = int(
        input(
            "What is the courier you would like to update? please give the number associated with the product "
        )
    )
    update_choice = int(
        input(
            (
                f"You selected {couriers_data[cour_update_input-1][cour_update_input][
            "Name"
        ]}, what would you like to update about it?\n1. Update Courier Name\n2.Update Courier Number\n"
            )
        )
    )
    if update_choice == 1:
        new_courier_name = input(
            f'Enter the new name you would like to give to {couriers_data[cour_update_input-1][cour_update_input][
            "Name"]} below\n> '
        )
        print(
            f'The new name for {couriers_data[cour_update_input-1][cour_update_input][
            "Name"]} will be {new_courier_name}, confirmed\n'
        )
        couriers_data[cour_update_input - 1][cour_update_input][
            "Name"
        ] = new_courier_name
    elif update_choice == 2:
        new_courier_num = input(
            f'Enter the new number you would like to give to {couriers_data[cour_update_input-1][cour_update_input][
            "Name"]}\nThe current number is {couriers_data[cour_update_input-1][cour_update_input][
            "Phone"]}\nEnter new number here (remember the number must start 020 and be 11 digits long) > '
        )
        if new_courier_num[0] == "0" and len(new_courier_num) == 11:
            print(
                f'The new number for {couriers_data[cour_update_input-1][cour_update_input][
                "Name"]} will be {new_courier_num}, confirmed\n'
            )
            couriers_data[cour_update_input - 1][cour_update_input][
                "Phone"
            ] = new_courier_num
        else:
            print("Thats and invalid input, please try again")
            courier_update()
    else:
        print("Thats and invalid input, please try again")
        courier_update()


# function to delete product


def prod_del():
    for prod in products_data:
        for index, value in prod.items():
            print(f'{index}. {value["Product"]} - £{value["Price"]}')
    prod_del_input = int(
        input(
            "What is the product you would like to delete? please give the number associated with the product "
        )
    )
    if prod_del_input <= len(products_data) and prod_del_input > 0:
        print(
            (
                f"You selected {products_data[prod_del_input - 1][prod_del_input]["Product"]}, This will now be removed from the list"
            )
        )
        del products_data[prod_del_input - 1]
    else:
        print("That's not a valid option please try again")
        prod_del()


# function for deleting an order


def delete_order():
    for order in orders:
        for key, value in order.items():
            print(
                f"\nOrder{key}: customer name: {value['customer_name']} status: {value['status']} items ordered: {value['items']} "
            )
    print("\n")
    del_order_input = int(
        input(
            "Which order would you like to delete, input the number with the corresponding order\n"
        )
    )
    print("\n")
    if del_order_input <= len(orders) and del_order_input > 0:
        orders.pop(del_order_input - 1)
        print(
            "confirmed, that order has been deleted, returning you to the the order menu"
        )
        orders_menu_opts()
    else:
        ("That is an invalid response, please try again")
        delete_order()


# function to delete a courier


def courier_del():
    for courier in couriers_data:
        for index, value in courier.items():
            print(f"{index}. {value["Name"]} - {value["Phone"]}")
    courier_del_input = int(
        input(
            "What is the courier you would like to delete? please give the number associated with the product "
        )
    )
    if courier_del_input <= len(couriers_data) and courier_del_input > 0:
        print(
            (
                f"You selected {couriers_data[courier_del_input-1][courier_del_input]["Name"]}, This courier will now be removed from the list"
            )
        )
        couriers_data.pop(courier_del_input - 1)
    else:
        print("That's not a valid option please try again")
        prod_del()


# function for printing out the up to date lists
def print_prod_list():
    for prod in products_data:
        for key, value in prod.items():
            print(f"Product {key}: {value['Product']} - £{value['Price']}")


def print_orders():
    for order in orders:
        for key, value in order.items():
            print(
                f"Order {key}: {value['customer_name']}, Items Order: {value['items']}, Status: {value['status']}"
            )


def print_couriers():
    for courier in couriers_data:
        for key, value in courier.items():
            print(f"Courier {key}: {value['Name']} - {value['Phone']}")


# main menu return prompt func
def mm_return_func():
    print("Input 0 if you'd like to now return to the main menu")
    mm_return_input = int(input())
    if mm_return_input == 0:
        logic_function()
    else:
        print("Thats not a valid option please try again")
        mm_return_func()


# Base logic func
def logic_function():
    main_menu_opts()
    first_input = int(
        input("Input the number corresponding with your desired option > ")
    )
    if first_input == 1:
        prod_file_open()
        products_menu_opts()
        prod_menu_input1 = int(
            input("Select the number associated with your desired option")
        )
        if prod_menu_input1 == 1:
            print_prod_list()
            mm_return_func()
        elif prod_menu_input1 == 2:
            add_product()
            products_persistance()
            mm_return_func()
        elif prod_menu_input1 == 3:
            prod_update()
            products_persistance()
            mm_return_func()
        elif prod_menu_input1 == 4:
            prod_del()
            products_persistance()
            mm_return_func()
        elif prod_menu_input1 == 0:
            logic_function()
    elif first_input == 3:
        order_file_open()
        orders_menu_opts()
        order_menu_input1 = int(
            input("\n Select the number associated with your desired option \n")
        )
        if order_menu_input1 == 1:
            print_orders()
            orders_persistance()
            mm_return_func()
        elif order_menu_input1 == 2:
            add_order_func()
            orders_persistance()
            mm_return_func()
        elif order_menu_input1 == 3:
            update_order_status()
            orders_persistance()
            mm_return_func()
        elif order_menu_input1 == 4:
            update_order()
            orders_persistance()
            mm_return_func()
        elif order_menu_input1 == 5:
            delete_order()
            orders_persistance()
            mm_return_func()
        elif order_menu_input1 == 0:
            logic_function()
    elif first_input == 2:
        courier_file_open()
        couriers_menu_options()
        courier_menu_input1 = int(
            input("\n Select the number associated with your desired option \n")
        )
        if courier_menu_input1 == 1:
            print_couriers()
            mm_return_func()
        elif courier_menu_input1 == 2:
            add_courier()
            couriers_persistance()
            mm_return_func()
        elif courier_menu_input1 == 3:
            courier_update()
            couriers_persistance()
            mm_return_func()
        elif courier_menu_input1 == 4:
            courier_del()
            couriers_persistance()
            mm_return_func()
        elif courier_menu_input1 == 0:
            logic_function()
    elif first_input == 0:
        print("you have decided to leave the app, goodbye")
    else:
        print("Thats not a valid option, try again")
        logic_function()


# app instantiation func
#logic_function()
