import data_module as data

# ---------------------------
# Module: Input/Output Handlers
# Provides functions for displaying data lists,
# capturing user selections, and formatting order output.
# ---------------------------

# ---------------------------
# Function: list_output
# Purpose: Display items from various data lists (products, couriers,
#          orders, or order status) with formatted headers.
# Arguments:
#   lst: one of data.products, data.couriers, data.orders, data.order_status
# ---------------------------
def list_output(lst):
    index_num = 1
    items_w_names = ""

    if lst == data.products:
        # Display product list with names and prices
        print(" \n-------\n-------")
        for item in lst:
            print(f"\n{index_num}. {item.get('name')} - £{item.get('price')}")
            index_num += 1
        print("-------\n-------")

    elif lst == data.couriers:
        # Display courier list with names and phone numbers
        print(" \n-------\n-------")
        for item in lst:
            print(f"\n{index_num}. {item.get('name')} - {item.get('phone_number')}")
            index_num += 1
        print("-------\n-------")

    elif lst == data.orders:
        # Display orders: customer details and product names
        for order in lst:
            inner_dict = next(iter(order.values()))  # Extract order details dict
            # Parse comma-separated product IDs into integers
            item_ids = [s.strip() for s in inner_dict["items"].split(",")]
            for id_str in item_ids:
                idx = int(id_str)
                items_w_names += f"\n{data.products[idx]['name']}"
            # Print order block
            print(
                f"-------\nOrder{index_num}:\n\n"
                f"Customer Name: {inner_dict['customer_name']}\n"
                f"Customer Address: {inner_dict['customer_address']}\n"
                f"Contact Number: {inner_dict['customer_phone']}\n"
                f"Status: {inner_dict['status']}\n"
                f"Courier: {data.couriers[int(inner_dict['courier'])]['name']} - "
                f"{data.couriers[int(inner_dict['courier'])]['phone_number']}\n"
                f"Items: \n{items_w_names}\n"
                "-------"
            )
            # Reset for next order
            items_w_names = ""
            index_num += 1

    elif lst == data.order_status:
        # Display available order status options
        print(" \n-------\n-------")
        for status in lst:
            print(f"\n{index_num}. {status}")
            index_num += 1
        print("-------\n-------")


# ---------------------------
# Function: list_input_function
# Purpose: Present a menu of items (products, couriers, orders,
#          or statuses) and capture valid user selection.
# Arguments:
#   lst: one of data.products, data.couriers, data.orders, data.order_status
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# Returns:
#   Integer index selected by the user
# ---------------------------
def list_input_function(lst, error_func, clear_func):
    index_num = 0
    items_w_names = ""
    while True:
        if lst == data.products:
            print(" \n-------\n-------")
            for item in lst:
                print(f"\n{index_num}. {item.get('name')} - £{item.get('price')}")
                index_num += 1
            print("-------\n-------")

        elif lst == data.couriers:
            print(" \n-------\n-------")
            for item in lst:
                print(f"\n{index_num}. {item.get('name')} - {item.get('phone_number')}")
                index_num += 1
            print("-------\n-------")

        elif lst == data.orders:
            print(" \n-------\n-------")
            for order in lst:
                inner = next(iter(order.values()))
                item_ids = [s.strip() for s in inner['items'].split(',')]
                for id_str in item_ids:
                    idx = int(id_str)
                    items_w_names += f"\n{data.products[idx]['name']}"
                print(
                    f"\n{index_num}. Order{index_num}:\n"
                    f"Customer Name: {inner['customer_name']}\n"
                    f"Items: {items_w_names}\n"
                    f"Status: {inner['status']}\n"
                    f"Courier: {data.couriers[int(inner['courier'])]['name']} - "
                    f"{data.couriers[int(inner['courier'])]['phone_number']}\n"
                    "-------"
                )
                items_w_names = ""
                index_num += 1
            print("-------\n-------")

        elif lst == data.order_status:
            print(" \n-------\n-------")
            for status in lst:
                print(f"\n{index_num}. {status}")
                index_num += 1
            print("-------\n-------")

        # Prompt the user for selection
        returned = input("\nWhich option above would you like to select?\n>>> ")
        clear_func()
        if error_func(returned, 0, len(lst) - 1):
            return int(returned)
        else:
            # Reset index if invalid and repeat
            index_num = 0


# ---------------------------
# Function: remove_order_output_function
# Purpose: Show items in an order and let the user pick one to remove.
# ---------------------------
def remove_order_output_function(items, products, error_func):
    # Remove formatting and split into individual IDs
    item_ids = [s for s in items.replace(',', '').split()]
    index_num = 0
    print("-------\n-------")
    while True:
        for id_str in item_ids:
            print(f"\n{index_num}. {products[int(id_str) - 1]['name']}")
            index_num += 1
        returned = input("\nWhich item above would you like to remove?\n>>> ")
        if error_func(returned, 0, len(products) - 1):
            return int(returned)
        else:
            index_num = 0


# ---------------------------
# Function: str_input_function
# Purpose: Display a list of string options and capture user choice.
# ---------------------------
def str_input_function(*options, error_func, clear_func):
    index_num = 0
    print("-------\n-------")
    while True:
        for opt in options:
            print(f"\n{index_num}. {opt}")
            index_num += 1
        returned = input(
            "\nWhich of the above options would you like to select?\n>>> "
        )
        clear_func()
        if error_func(returned, 0, len(options) - 1):
            return int(returned)
        else:
            index_num = 0


# ---------------------------
# Function: order_custom_output_function
# Purpose: Print detailed order information based on view_option.
# ---------------------------
def order_custom_output_function(orderslist, view_option, prodlist):
    index_num = 1
    items_w_names = ""
    if int(view_option) == 1:
        # Show basic order summary
        for order in orderslist:
            inner = next(iter(order.values()))
            item_ids = [s.strip() for s in inner['items'].split(',')]
            for id_str in item_ids:
                items_w_names += f"\n{prodlist[int(id_str)]['name']}"
            print(
                f"-------\nOrder{index_num}:\n\n"
                f"Customer Name: {inner['customer_name']}\n"
                f"Items: {items_w_names}\n"
                f"Status: {inner['status']}\n"
                "-------"
            )
            items_w_names = ""
            index_num += 1

    elif int(view_option) == 2:
        # Show order with courier details
        for order in orderslist:
            inner = next(iter(order.values()))
            item_ids = [s.strip() for s in inner['items'].split(',')]
            for id_str in item_ids:
                items_w_names += f"\n{prodlist[int(id_str)]['name']}"
            print(
                f"-------\nOrder{index_num}:\n\n"
                f"Customer Name: {inner['customer_name']}\n"
                f"Items: {items_w_names}\n"
                f"Courier: {data.couriers[int(inner['courier'])]['name']} - "
                f"{data.couriers[int(inner['courier'])]['phone_number']}\n"
                "-------"
            )
            items_w_names = ""
            index_num += 1
