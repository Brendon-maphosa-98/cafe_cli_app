import re

# ---------------------------
# Module: Order Menu Actions
# Provides functions to add, remove, update, and delete orders
# within the in-memory orders list.
# ---------------------------


# ---------------------------
# Function: add_item
# Purpose: Add product items to an existing order by prompting user selections.
# Arguments:
#   list_input_func: function to display and select products
#   prodlist: list of all products
#   error_func: function to validate numeric input
#   ordernum: integer order number (1-based) to modify
#   clear_func: function to clear the console screen
#   orderslist: list of order dicts
# Returns:
#   A comma-separated string of updated item IDs for the order
# ---------------------------
def add_item(list_input_func, prodlist, error_func, ordernum, clear_func, orderslist):
    temp_orders_list = orderslist
    # Extract current items IDs from the selected order
    current_items = [
        item
        for item in (
            temp_orders_list[ordernum - 1][ordernum]["items"]
            .replace(",", "")
            .replace(" ", "")
        )
    ]
    selected_items = []
    final_items = ""
    # Loop until user finishes adding
    while True:
        item_selected = list_input_func(prodlist, error_func, clear_func)
        # Ask if user wants to continue adding
        option2 = input(
            f"You have selected to add {prodlist[item_selected]['name']} to order{ordernum}\n"
            "Would you like to add another item? 1: Yes 2: No\n>>> "
        )
        if error_func(option2, 1, 2):
            if int(option2) == 1:
                selected_items.append(prodlist[item_selected]["name"])
                current_items.append(prodlist.index(prodlist[item_selected]))
            else:
                # Finalize additions
                selected_items.append(prodlist[item_selected]["name"])
                current_items.append(prodlist.index(prodlist[item_selected]))
                print(f"Items added to order{ordernum}: {selected_items}")
                # Build comma-separated ID string
                final_items = ", ".join(str(i) for i in current_items)
                return final_items
        else:
            print("Invalid input, please try again.")


# ---------------------------
# Function: remove_item
# Purpose: Remove product items from an existing order.
# Arguments:
#   orderslist: list of order dicts
#   ordernum: integer order number (1-based)
#   prodlist: list of all products
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# Returns:
#   Updated orderslist with modified items
# ---------------------------
def remove_item(orderslist, ordernum, prodlist, error_func, clear_func):
    temp_orders_list = orderslist
    # Extract current items string and convert to list of characters (IDs)
    items = (
        temp_orders_list[ordernum - 1][ordernum]["items"]
        .replace(",", "")
        .replace(" ", "")
    )
    itemslist = [item for item in items]
    # Loop until removal complete
    while True:
        # Display current items
        for item in itemslist:
            print(f"{item}. {prodlist[int(item)]['name']}")
        removing_item = input("Which product number would you like to remove?\n>>> ")
        if (
            error_func(removing_item, 0, len(prodlist) - 1)
            and removing_item in itemslist
        ):
            itemslist.remove(removing_item)
            # Ask if more removals
            remove_more = input(
                f"Removed {prodlist[int(removing_item)]['name']}. Remove another? 1:Yes 2:No\n>>> "
            )
            if error_func(remove_more, 1, 2) and remove_more == "1":
                continue
            elif error_func(remove_more, 1, 2) and remove_more == "2":
                # Update order items
                temp_orders_list[ordernum - 1][ordernum]["items"] = ", ".join(itemslist)
                return temp_orders_list
            else:
                print("Please try again.")
        else:
            clear_func()
            print("Invalid input, please try again.\n")


# ---------------------------
# Function: add_order
# Purpose: Collect new order details interactively and append to orderslist.
# ---------------------------
def add_order(
    orderslist,
    status_opt_list,
    clear_func,
    list_input_func,
    prodlist,
    error_func,
    courlist,
):
    # Gather customer name
    while True:
        fname = input("Enter customer's first name:\n>>> ")
        lname = input("Enter customer's last name:\n>>> ")
        if re.match(r"^[A-Za-z\s\-]+$", fname) and re.match(r"^[A-Za-z\s\-]+$", lname):
            cust_name = f"{fname.strip().title()} {lname.strip().title()}"
            clear_func()
            break
        print("Invalid name. Letters, spaces, hyphens only.")

    # Gather customer address
    while True:
        street = input("Enter delivery street:\n>>> ")
        city = input("Enter delivery city:\n>>> ")
        if not re.search(
            r"[0-9]|[!@#$%^*()=+{}\[\]|;:'\"<>,.?~`]", street
        ) and not re.search(r"[0-9]|[!@#$%^*()=+{}\[\]|;:'\"<>,.?~`]", city):
            cust_addr = f"{street.strip().title()}, {city.strip().upper()}"
            break
        clear_func()
        print("Invalid address. No digits or special chars.")

    # Gather customer phone number
    while True:
        phone = input("Enter customer mobile (11 digits, starts 0):\n>>> ")
        if re.match(r"^0\d{10}$", phone):
            break
        clear_func()
        print("Invalid phone number.")

    # Gather order items
    clear_func()
    items_str = ""
    placing = True
    while placing:
        print("Select items to add:")
        choice = list_input_func(prodlist, error_func, clear_func)
        items_str += f"{choice}, "
        more = input("Add another? 1:Yes 2:No\n>>> ")
        if not (error_func(more, 1, 2) and more == "1"):
            placing = False
    items_str = items_str.rstrip(", ")

    # Choose courier
    clear_func()
    print("Select courier:")
    cidx = list_input_func(courlist, error_func, clear_func)

    # Build and append new order
    new_order_id = len(orderslist) + 1
    orderslist.append(
        {
            new_order_id: {
                "customer_name": cust_name,
                "customer_address": cust_addr,
                "customer_phone": phone,
                "status": status_opt_list[0],
                "courier": cidx,
                "items": items_str,
            }
        }
    )
    return orderslist


# ---------------------------
# Function: update_existing_order_status
# Purpose: Change the status of a selected order.
# ---------------------------
def update_existing_order_status(
    list_output_func,
    orderslist,
    error_func,
    list_input_func,
    status_opt_list,
    clear_func,
):
    while True:
        clear_func()
        list_output_func(orderslist)
        sel = input("Select order number to change status:\n>>> ")
        if error_func(sel, 1, len(orderslist)):
            order_idx = int(sel)
            clear_func()
            status_idx = list_input_func(status_opt_list, error_func, clear_func)
            orderslist[order_idx - 1][order_idx]["status"] = status_opt_list[status_idx]
            return orderslist


# ---------------------------
# Function: update_existing_order
# Purpose: Update various fields of a selected order interactively.
# ---------------------------
def update_existing_order(
    orderslist,
    error_func,
    str_input_func,
    prodlist,
    list_output_func,
    list_input_func,
    clear_func,
    courlist,
):
    temp_orders_list = orderslist
    loop = 1
    clear_func()
    while loop == 1:

        list_output_func(temp_orders_list)
        chng_sel1 = input("Which of the above options whould you like to select?\n>>> ")
        chng_sel2 = error_func(
            chng_sel1,
            1,
            len(temp_orders_list),
        )
        clear_func()
        if chng_sel2:
            chng_sel1 = int(chng_sel1)
            chng_op1 = str_input_func(
                "Change customer name",
                "Change delivery address",
                "Change customer phone number",
                "Add items to order",
                "Remove items from order",
                "Change the courier assigned to an order",
                error_func=error_func,
                clear_func=clear_func,
            )
            loop2 = 1
            clear_func()
            if chng_op1 == 0:  # name
                while loop2 == 1:
                    customer_name1 = input(
                        "\nPlease enter the new name first name of the customer\n>>> "
                    )
                    customer_name2 = input(
                        "\nPlease enter the new name second name of the customer\n>>> "
                    )
                    if (
                        bool(re.search("^[a-zA-Z\s\-]+$", customer_name1)) == False
                        or bool(re.search("^[a-zA-Z\s\-]+$", customer_name2)) == False
                        or bool(re.search("^[\s]+", customer_name1)) == True
                        or bool(re.search("^[\s]+", customer_name2)) == True
                    ):
                        clear_func()
                        print(
                            "The customer first or last name are required and cannot start with a space and can only contain letters, please try again"
                        )
                        loop2 == 1
                    else:
                        clear_func()
                        print(
                            f"The new customer name for order{chng_sel1} is {customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}\n"
                        )
                        temp_orders_list[chng_sel1 - 1][chng_sel1][
                            "customer_name"
                        ] = f"{customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 1:  # address
                while loop2 == 1:
                    customer_address1 = input(
                        "\nPlease enter the new name of the street for delivery\n>>> "
                    )
                    customer_address2 = input(
                        "\nPlease enter the new name of city for delivery\n>>> "
                    )
                    if (
                        bool(re.search("[0-9]", customer_address1)) == True
                        or bool(re.search("[0-9]", customer_address2)) == True
                        or bool(re.search("^[\s]+", customer_address1)) == True
                        or bool(re.search("^[\s]+", customer_address1)) == True
                        or bool(
                            re.search(
                                r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~]", customer_address1
                            )
                        )
                        == True
                        or bool(
                            re.search(
                                r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~]", customer_address2
                            )
                        )
                        == True
                    ):
                        clear_func()
                        print(
                            "The delivery street name or city are required and cannot contain any numbers,special characters (!@# ect) or start with a space, please try again"
                        )
                        loop2 == 1
                    else:
                        clear_func()
                        print(
                            f"The new address for order{chng_sel1} is {customer_address1.title().strip()}, {customer_address2.upper().strip()} confirmed"
                        )
                        temp_orders_list[chng_sel1 - 1][chng_sel1][
                            "customer_address"
                        ] = f"{customer_address1.title().strip()}, {customer_address2.upper().strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 2:  # phone
                while loop2 == 1:
                    customer_number = input(
                        "\nPlease enter the new mobile number for the customer\n>>> "
                    )
                    if (
                        bool(re.search("[a-zA-Z]", customer_number)) == True
                        or len(customer_number) != 11
                        or bool(re.search("^[\s]+", customer_number)) == True
                        or customer_number[0] != "0"
                    ):
                        clear_func()
                        print(
                            "The customers phone number is required and cannot contain any letters or start with a space and must be 11 digits long and must start with a 0, please try again"
                        )
                        loop2 == 1
                    else:
                        clear_func()
                        print(
                            f"The new number for order{chng_sel1} is {customer_number.strip()} confirmed"
                        )
                        temp_orders_list[chng_sel1 - 1][chng_sel1][
                            "customer_phone"
                        ] = f"{customer_number.strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 3:  # add items
                temp_orders_list[chng_sel1 - 1][chng_sel1]["items"] = add_item(
                    list_input_func,
                    prodlist,
                    error_func,
                    chng_sel1,
                    clear_func,
                    orderslist,
                )
                loop += 1
                return temp_orders_list
            elif chng_op1 == 4:  # remove items
                temp_orders_list = remove_item(
                    orderslist,
                    int(chng_sel1),
                    prodlist,
                    error_func,
                    clear_func,
                )
                loop += 1
                return temp_orders_list
            elif chng_op1 == 5:  # courier
                temp_orders_list = orderslist
                print(f"Below are the couriers available for order{chng_sel1}:")
                courier_change_selection = list_input_func(
                    courlist, error_func, clear_func
                )
                print(
                    f"You have selected to add {courlist[courier_change_selection]['name']} as the courier for order{chng_sel1}\n"
                )
                temp_orders_list[chng_sel1 - 1][chng_sel1][
                    "courier"
                ] = courier_change_selection
                loop += 1
                return temp_orders_list
        else:
            loop == 1
    else:
        return temp_orders_list


# ---------------------------
# Function: del_order
# Purpose: Delete an order based on user selection.
# ---------------------------
def del_order(orderslist, list_output_func, error_func, clear_func):
    while True:
        clear_func()
        list_output_func(orderslist)
        sel = input("Select order to delete:\n>>> ")
        if error_func(sel, 1, len(orderslist)):
            idx = int(sel) - 1
            clear_func()
            print(f"Order {sel} removed.\n")
            orderslist.pop(idx)
            return orderslist
        # loop until valid
