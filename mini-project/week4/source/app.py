import random
import csv


# Print main menu options
def main_menu_opts():
    print(
        "welcome to the main menu, what would you like to do:\n1: Print Products Menu,\n2: Print Orders Menu,\n3: Print Couriers Menu\n0: Exit app"
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


# creating initial orders list containing dictionary of orders

orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
            "Courier": "Just Eat",
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "item(s)_ordered": ["Flat White", "Croissant"],
            "Courier": "Deliveroo",
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
            "Courier": "Uber",
        }
    },
]

# empty variables to hold the imported data from the txt files locally in python
products_data = {}

couriers_data = {}

orders = []

# open() functions to import and read to empty variables the data from the csv files
with open("mini-project/week4/data/products.csv") as temp_products_data:
    reader = csv.DictReader(temp_products_data)
    for row in reader:
        products_data[int(row["Index"])] = row["Product"]

with open("mini-project/week4/data/couriers.csv") as temp_couriers_data:
    reader = csv.DictReader(temp_couriers_data)
    for row in reader:
        couriers_data[int(row["Index"])] = row["Name"]

with open("mini-project/week4/data/orders.csv") as temp_orders_data:
    reader = csv.DictReader(temp_orders_data)
    temp_dict = {}
    for row in reader:
        temp_dict = dict(
            customer_name=row["customer_name"],
            customer_address=row["customer_address"],
            customer_phone=row["customer_phone"],
            courier=int(row["courier"]),
            status=row["status"],
            items=row["items"],
        )
        orders.append({int(row["order_num"]): temp_dict})


# function for add new products to the products data file
def add_product():
    global products_data
    new_product = input("what is the new product you would like to add?\n")
    products_data.update({len(products_data) + 1: f"{new_product}"})


# data persistance elements for couriers and products


def products_persistance():
    with open(
        "mini-project/week4/data/products.csv", "w"
    ) as temp_updated_products_data:
        fieldnames = ["Index", "Product"]
        writer = csv.DictWriter(temp_updated_products_data, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in products_data.items():
            writer.writerow({"Index": key, "Product": value})


def couriers_persistance():
    with open(
        "mini-project/week4/data/couriers.csv", "w"
    ) as temp_updated_couriers_data:
        fieldnames = ["Index", "Courier"]
        writer = csv.DictWriter(temp_updated_couriers_data, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in couriers_data.items():
            writer.writerow({"Index": key, "Courier": value})


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
                writer.writerow(
                    {
                        "order_num": int(key),
                        "customer_name": value["customer_name"],
                        "customer_address": value["customer_address"],
                        "customer_phone": value["customer_phone"],
                        "courier": value["courier"],
                        "status": value["status"],
                        "items": value["items"],
                    }
                )


# function for creating a new courier


def add_courier():
    global couriers_data
    new_courier = input("what is the new courier you would like to add?\n")
    couriers_data.update({len(couriers_data) + 1: f"{new_courier}"})


# function for adding a new order


def add_order_func():
    global orders
    global products_data
    global couriers_data
    ordernum = random.randint(0, 100)
    customername = input("please enter the customers name > ")
    customeraddress = input("please enter the street and city of the customer > ")
    customerphone = int(input("Please enter the customers phone number > "))
    num = 1
    for x in products_data:
        print(f"{num}.{x}\n")
        num += 1
    selected_items = []

    def item_selection():
        itemorderedinput = int(
            input(
                "Please select the item(s) the customer would like to order - (input the number corresponding with the desired item, if order more than one item, enter the first one and wait to be prompted for subsequent item selections > "
            )
        )
        itemorderedinput -= 1
        confirmation_input = int(
            input(
                f"you have selected {products_data[itemorderedinput]}, How would you like to proceed - \n 1 - add {products_data[itemorderedinput]} to order and confirm item's selection \n 2 - add {products_data[itemorderedinput]} to order and add another item \n 3 - don't add {products_data[itemorderedinput]} and return to the orders menu > "
            )
        )
        if confirmation_input == 1:
            selected_items.append(products_data[itemorderedinput])
            print(
                f"Confirmed, the following items have been added to the order {str(selected_items)}"
            )
        elif confirmation_input == 2:
            selected_items.append(products_data[itemorderedinput])
            item_selection()
        elif confirmation_input == 3:
            orders_menu_opts
        else:
            print("Thats an invalid response, please try again")
            item_selection()

    item_selection()

    num = 1
    for courier in couriers_data:
        print(f"{num}. {courier}")
        num += 1
    courier_choice = int(
        input(
            "\nFrom the list above, please select the courier you would like to assign to the order"
        )
    )
    courier_selection = couriers_data[courier_choice - 1]

    new_order = {
        f"order{ordernum}": {
            "customer_name": customername,
            "customer_address": customeraddress,
            "customer_phone": customerphone,
            "status": "preparing",
            "item(s)_ordered": selected_items,
            "Courier": courier_selection,
        }
    }
    print(
        f"\n This is your new order which has now been added to the orders list > {new_order}"
    )
    orders.append(new_order)


# function for updating an existing order status

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]


def update_order_status():
    global orders
    global order_status
    for order in orders:
        num = 1
        for order_num, order_detail in order.items():
            print(f"{num}.{order_num}: status: {order_detail['status']}")
            num += 1
    print("\n")
    change_selection1 = int(
        input(
            "Which order would like to update the status for? input the number for the associated order > "
        )
    )
    print(
        f"what would you like to change {orders[change_selection1 -1].keys()} to? below is the available options"
    )
    for status in order_status:
        num = 1
        print(f"{num}. {status}")
        num += 1
    change_selection2 = int(
        input(
            f"whats the number associated with the status you would like to update {orders[change_selection1 -1].keys()} to?"
        )
    )

    if change_selection2 <= 4:
        for order_key in orders[change_selection1 - 1].keys():
            orders[change_selection1 - 1][order_key]["status"] = order_status[
                change_selection2 - 1
            ]
        print(orders)


# function for updating existing order


def update_order():
    global orders
    global products_data
    dict_key_directory = [
        "customer_name",
        "customer_address",
        "customer_phone",
        "status",
        "item(s)_ordered",
        "Courier",
    ]
    for order in orders:
        for order_num, order_detail in order.items():
            print(
                f"{orders.index(order) + 1}.{order_num}: customer name: {order_detail['customer_name']} status: {order_detail['status']} items ordered: {order_detail['item(s)_ordered']} Courier: {order_detail['Courier']} "
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
        orders[change_selection1 - 1][order_key][
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

            def add_item():
                num = 1
                for prod in products_data:
                    print(f"{num}.{prod}\n")
                num += 1
                for key in orders[change_selection1 - 1].keys():
                    order_key = key
                itemorderedinput = int(
                    input(
                        "Please select the item(s) the customer would like to add to the order - (input the number corresponding with the desired item, if order more than one item, enter the first one and wait to be prompted for subsequent item selections > "
                    )
                )
                itemorderedinput -= 1
                confirmation_input = int(
                    input(
                        f"you have selected {products_data[itemorderedinput]}, How would you like to proceed - \n 1 - add {products_data[itemorderedinput]} to order and confirm item's selection \n 2 - add {products_data[itemorderedinput]} to order and add another item \n 3 - don't add {products_data[itemorderedinput]} and return to the orders menu > "
                    )
                )
                if confirmation_input == 1:
                    selected_items.append(products_data[itemorderedinput])
                    print(
                        f"Confirmed, the following items have been added to the order: {str(selected_items)}"
                    )
                    orders[change_selection1 - 1][order_key][
                        dict_key_directory[change_selection2 - 1]
                    ].append(selected_items)
                elif confirmation_input == 2:
                    selected_items.append(products_data[itemorderedinput])
                    add_item()
                elif confirmation_input == 3:
                    orders_menu_opts
                else:
                    print("Thats an invalid response, please try again")
                    add_item()

            add_item()
        elif order_update_input == 2:

            def rmv_order_item():
                order_temp_items = orders[change_selection1 - 1][order_key][
                    dict_key_directory[change_selection2 - 1]
                ]
                num = 1
                for order in order_temp_items:
                    print(f"Below are the items that {order_num} currently has\n")
                    print(f"{num}.{order}\n")
                    num += 1
                for key in orders[change_selection1 - 1].keys():
                    order_key = key
                itemorderedinput = int(
                    input(
                        "Please select the item(s) the customer would like to remove from the order - (input the number corresponding with the desired item, if order more than one item, enter the first one and wait to be prompted for subsequent item selections > "
                    )
                )
                itemorderedinput -= 1
                confirmation_input = int(
                    input(
                        f"you have selected {products_data[itemorderedinput]}, How would you like to proceed - \n 1 - remove {products_data[itemorderedinput]} from order and confirm item's remove \n 2 - add {products_data[itemorderedinput]} to order and remove another item \n 3 - don't remove {products_data[itemorderedinput]} and return to the orders menu > "
                    )
                )
                if confirmation_input == 1:
                    orders[change_selection1 - 1][order_key][
                        dict_key_directory[change_selection2 - 1]
                    ].pop(itemorderedinput)
                if confirmation_input == 2:
                    orders[change_selection1 - 1][order_key][
                        dict_key_directory[change_selection2 - 1]
                    ].pop(itemorderedinput)
                    rmv_order_item()
                if confirmation_input == 3:
                    orders_menu_opts()
                else:
                    print("Thats an invalid response, please try again")
                    rmv_order_item()

    elif change_selection2 == 6:
        num = 1
        for courier in couriers_data:
            print(f"{num}. {courier}")
            num += 1
        for key in orders[change_selection1 - 1].keys():
            order_key = key
        change_selection3 = int(
            input(
                f"which courier from the ones listed above would you like to change the courier of order {order_num} to?, input the number of the courier below\n> "
            )
        )
        orders[change_selection1 - 1][order_key][
            dict_key_directory[change_selection2 - 1]
        ] = couriers_data[change_selection3 - 1]


# function for updating existing product
def prod_update():
    for index, value in products_data.items():
        print(f"{index}. {value}")
    prod_update_input = int(
        input(
            "What is the product you would like to update? please give the number associated with the product\n"
        )
    )
    if prod_update_input <= len(products_data):
        new_update_val = input(
            (
                f"You selected {products_data[prod_update_input]}, what would you like to update it to?\n"
            )
        )
        products_data[prod_update_input] = new_update_val
    else:
        print("That's not a valid option please try again\n")
        prod_update()


# function for updating courier information


def courier_update():
    for index, value in couriers_data.items():
        print(f"{index}. {value}")
    cour_update_input = int(
        input(
            "What is the courier you would like to update? please give the number associated with the product "
        )
    )
    if cour_update_input <= len(couriers_data):
        new_update_val = input(
            (
                f"You selected {couriers_data[cour_update_input]}, what would you like to update it to? "
            )
        )
        couriers_data[cour_update_input] = new_update_val
    else:
        print("That's not a valid option please try again")
        courier_update()


# function to delete product


def prod_del():
    for index, value in products_data.items():
        print(f"{index}. {value}")
    prod_del_input = int(
        input(
            "What is the product you would like to delete? please give the number associated with the product "
        )
    )
    if prod_del_input <= len(products_data) and prod_del_input > 0:
        print(
            (
                f"You selected {products_data[prod_del_input]}, This will now be removed from the list"
            )
        )
        del products_data[prod_del_input]
    else:
        print("That's not a valid option please try again")
        prod_del()


# function for deleting an order


def delete_order():
    for order in orders:
        for order_num, order_detail in order.items():
            print(
                f"{orders.index(order) + 1}.{order_num}: customer name: {order_detail['customer_name']} status: {order_detail['status']} items ordered: {order_detail['item(s)_ordered']} "
            )
    print("\n")
    del_order_input = int(
        input(
            "Which order would you like to delete, input the number with the corresponding order\n"
        )
    )
    print("\n")
    if del_order_input <= len(orders):
        order_detail = list(orders[del_order_input - 1].keys())
        del_order_input - 1
        orders.pop(orders.index(orders[del_order_input - 1]))
        print(
            "confirmed, that order has been deleted, returning you to the the order menu"
        )
        orders_menu_opts()
    else:
        ("That is an invalid response, please try again")
        delete_order()


# function to delete a courier


def courier_del():
    for index, value in couriers_data.items():
        print(f"{index}. {value}")
    courier_del_input = int(
        input(
            "What is the courier you would like to delete? please give the number associated with the product "
        )
    )
    if courier_del_input <= len(couriers_data) and courier_del_input > 0:
        print(
            (
                f"You selected {couriers_data[courier_del_input]}, This will now be removed from the list"
            )
        )
        del couriers_data[courier_del_input]
    else:
        print("That's not a valid option please try again")
        prod_del()


# function for printing out the up to date lists
def print_prod_list():
    print(products_data)


def print_orders():
    print(orders)


def print_couriers():
    print(couriers_data)


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
    # return_frm_txt()  #return_frm_txt() # Commented out from V1 as data persistance is not possible from what I know without an external data storage file.
    main_menu_opts()
    first_input = int(
        input("Input the number corresponding with your desired option > ")
    )
    # while first_input >= 1 : # tested in test enviroment without this while loop and code look's like it works as normal so this is actually not necessery.
    if first_input == 1:
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
            logic_function
    elif first_input == 2:
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
    elif first_input == 3:
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
# logic_function()
