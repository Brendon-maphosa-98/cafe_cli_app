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
        clear_func()
        fname = input("Enter customer's first name:\n>>> ")
        lname = input("Enter customer's last name:\n>>> ")
        if re.match(r"^[A-Za-z\s\-]+$", fname) and re.match(r"^[A-Za-z\s\-]+$", lname):
            cust_name = f"{fname.strip().title()} {lname.strip().title()}"
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
        clear_func()
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
    str_input_function,
    prodlist,
    list_output_func,
    list_input_func,
    clear_func,
    courlist,
):
    while True:
        clear_func()
        list_output_func(orderslist)
        sel = input("Select order to update:\n>>> ")
        if error_func(sel, 1, len(orderslist)):
            order_idx = int(sel)
            # Choose which field to update
            opt = str_input_function(
                "Change name",
                "Change address",
                "Change phone",
                "Add items",
                "Remove items",
                "Change courier",
                error_func=error_func,
                clear_func=clear_func,
            )
            clear_func()
            if opt == 0:  # name
                ...  # similar pattern as add_order
            elif opt == 1:  # address
                ...
            elif opt == 2:  # phone
                ...
            elif opt == 3:  # add items
                orderslist = add_item(...)
            elif opt == 4:  # remove items
                orderslist = remove_item(...)
            elif opt == 5:  # courier
                cidx = list_input_func(courlist, error_func, clear_func)
                orderslist[order_idx - 1][order_idx]["courier"] = cidx
            return orderslist


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
