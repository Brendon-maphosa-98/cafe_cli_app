import data_module as data

# ---------------------------
# Module: Navigation Menu Handlers
# Provides functions to navigate between menus,
# including returning to a previous menu and the
# product management submenu loop.
# ---------------------------


# ---------------------------
# Function: rtrn_opt
# Purpose: Prompt the user to input 0 to return to the previous menu
# Arguments:
#   clear_func: function to clear the console screen
# Returns:
#   Integer 0 when the user confirms return
# ---------------------------
def rtrn_opt(clear_func):
    loop = True
    while loop:
        try:
            # Prompt user for return option
            rtrn = int(
                input(
                    "-----------------\n\n" "Input 0 to return to the previous menu\n\n"
                )
            )
            if rtrn == 0:
                # Valid return, exit loop and return value
                return rtrn
            else:
                clear_func()
                print(
                    "\nThat is an invalid option, you must enter the number 0, please try again\n"
                )
        except ValueError:
            # Handle non-integer inputs gracefully
            clear_func()
            print(
                "You entered an invalid input, you must enter the number 0, please try again\n"
            )
        # Loop continues until a valid 0 is entered


# ---------------------------
# Function: product_loop
# Purpose: Display and handle the product submenu choices
#          including viewing, adding, updating, and deleting products.
# Arguments:
#   str_input_func: function to display string menu options and capture selection
#   list_output_func: function to display a list of products
#   prodlist: list of product dicts
#   new_product_func: function to add a new product
#   update_item_func: function to update an existing product
#   del_item_func: function to delete a product
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# ---------------------------
def product_loop(
    str_input_func,
    list_output_func,
    prodlist,
    new_product_func,
    update_item_func,
    del_item_func,
    error_func,
    clear_func,
):
    loop = True
    while loop:
        clear_func()
        # Show product menu options and get user's choice
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the products list",
            "Add a new product",
            "Update an existing product",
            "Remove an existing product",
            error_func=error_func,
            clear_func=clear_func,
        )
        clear_func()

        # View products
        if Menu_choice == 1:
            list_output_func(prodlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Add a new product
        elif Menu_choice == 2:
            prodlist = new_product_func(prodlist, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Update an existing product
        elif Menu_choice == 3:
            prodlist = update_item_func(
                list_output_func,
                prodlist,
                error_func,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Remove an existing product
        elif Menu_choice == 4:
            prodlist = del_item_func(list_output_func, prodlist, error_func, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Exit to main menu
        elif Menu_choice == 0:
            clear_func()
            break


# ---------------------------
# Module: Navigation Menu Handlers
# Provides functions to navigate between menus,
# including returning to a previous menu and the
# product management submenu loop.
# ---------------------------


# ---------------------------
# Function: rtrn_opt
# Purpose: Prompt the user to input 0 to return to the previous menu
# Arguments:
#   clear_func: function to clear the console screen
# Returns:
#   Integer 0 when the user confirms return
# ---------------------------
def rtrn_opt(clear_func):
    loop = True
    while loop:
        try:
            # Prompt user for return option
            rtrn = int(
                input(
                    "-----------------\n\n" "Input 0 to return to the previous menu\n\n"
                )
            )
            if rtrn == 0:
                # Valid return, exit loop and return value
                return rtrn
            else:
                clear_func()
                print(
                    "\nThat is an invalid option, you must enter the number 0, please try again\n"
                )
        except ValueError:
            # Handle non-integer inputs gracefully
            clear_func()
            print(
                "You entered an invalid input, you must enter the number 0, please try again\n"
            )
        # Loop continues until a valid 0 is entered


# ---------------------------
# Function: product_loop
# Purpose: Display and handle the product submenu choices
#          including viewing, adding, updating, and deleting products.
# Arguments:
#   str_input_func: function to display string menu options and capture selection
#   list_output_func: function to display a list of products
#   prodlist: list of product dicts
#   new_product_func: function to add a new product
#   update_item_func: function to update an existing product
#   del_item_func: function to delete a product
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# ---------------------------
def product_loop(
    str_input_func,
    list_output_func,
    prodlist,
    new_product_func,
    update_item_func,
    del_item_func,
    error_func,
    clear_func,
):
    loop = True
    while loop:
        clear_func()
        # Show product menu options and get user's choice
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the products list",
            "Add a new product",
            "Update an existing product",
            "Remove an existing product",
            error_func=error_func,
            clear_func=clear_func,
        )
        clear_func()

        # View products
        if Menu_choice == 1:
            list_output_func(prodlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Add a new product
        elif Menu_choice == 2:
            prodlist = new_product_func(prodlist, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Update an existing product
        elif Menu_choice == 3:
            prodlist = update_item_func(
                list_output_func,
                prodlist,
                error_func,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Remove an existing product
        elif Menu_choice == 4:
            prodlist = del_item_func(list_output_func, prodlist, error_func, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Exit to main menu
        elif Menu_choice == 0:
            clear_func()
            break

    # End of product submenu loop


# ---------------------------
# Function: Orders_loop
# Purpose: Display and handle the orders submenu choices including viewing,
#          filtering, adding, updating, and deleting orders.
# Arguments:
#   str_input_func: function to display string menu options
#   error_func: function to validate numeric input
#   list_output_func: function to list raw order entries
#   orderslist: list of order dicts
#   add_order_func: function to add a new order
#   update_existing_order_status_func: function to change order status
#   status_opt_list: list of possible order statuses
#   update_existing_order_func: function to modify order details
#   del_order_func: function to delete an order
#   list_input_func: function to select items and couriers
#   prodlist: list of all products
#   clear_func: function to clear the console screen
#   courlist: list of couriers
#   order_custom_output_function: function to show formatted orders
# ---------------------------
def Orders_loop(
    str_input_func,
    error_func,
    list_output_func,
    orderslist,
    add_order_func,
    update_existing_order_status_func,
    status_opt_list,
    update_existing_order_func,
    del_order_func,
    list_input_func,
    prodlist,
    clear_func,
    courlist,
    order_custom_output_function,
):
    loop1 = 1
    while loop1 == 1:
        clear_func()
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the orders list",
            "view the orders list by assigned courier",
            "view the orders list by status",
            "Add a new order",
            "Update the status of an order",
            "Update an existing order",
            "Remove an existing order",
            error_func=error_func,
            clear_func=clear_func,
        )
        if Menu_choice == 1:
            clear_func()
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
            else:
                clear_func()
                None
        elif Menu_choice == 2:
            order_custom_output_function(
                orderslist,
                2,
                prodlist,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            order_custom_output_function(
                orderslist,
                1,
                prodlist,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 4:
            clear_func()
            orderslist = add_order_func(
                orderslist,
                status_opt_list,
                clear_func,
                list_input_func,
                prodlist,
                error_func,
                courlist,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 5:
            clear_func()
            orderslist = update_existing_order_status_func(
                list_output_func,
                orderslist,
                error_func,
                list_input_func,
                status_opt_list,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 6:
            clear_func()
            orderslist = update_existing_order_func(
                orderslist,
                error_func,
                str_input_func,
                prodlist,
                list_output_func,
                list_input_func,
                clear_func,
                courlist,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 7:
            clear_func()
            orderslist = del_order_func(
                orderslist, list_output_func, error_func, clear_func
            )
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 0:
            clear_func()
            loop1 += 1

    # End of orders submenu loop


# ---------------------------
# Module: Navigation Menu Handlers
# Provides functions to navigate between menus,
# including returning to a previous menu and the
# product management submenu loop.
# ---------------------------


# ---------------------------
# Function: rtrn_opt
# Purpose: Prompt the user to input 0 to return to the previous menu
# Arguments:
#   clear_func: function to clear the console screen
# Returns:
#   Integer 0 when the user confirms return
# ---------------------------
def rtrn_opt(clear_func):
    loop = True
    while loop:
        try:
            # Prompt user for return option
            rtrn = int(
                input(
                    "-----------------\n\n" "Input 0 to return to the previous menu\n\n"
                )
            )
            if rtrn == 0:
                # Valid return, exit loop and return value
                return rtrn
            else:
                clear_func()
                print(
                    "\nThat is an invalid option, you must enter the number 0, please try again\n"
                )
        except ValueError:
            # Handle non-integer inputs gracefully
            clear_func()
            print(
                "You entered an invalid input, you must enter the number 0, please try again\n"
            )
        # Loop continues until a valid 0 is entered


# ---------------------------
# Function: product_loop
# Purpose: Display and handle the product submenu choices
#          including viewing, adding, updating, and deleting products.
# Arguments:
#   str_input_func: function to display string menu options and capture selection
#   list_output_func: function to display a list of products
#   prodlist: list of product dicts
#   new_product_func: function to add a new product
#   update_item_func: function to update an existing product
#   del_item_func: function to delete a product
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# ---------------------------
def product_loop(
    str_input_func,
    list_output_func,
    prodlist,
    new_product_func,
    update_item_func,
    del_item_func,
    error_func,
    clear_func,
):
    loop = True
    while loop:
        clear_func()
        # Show product menu options and get user's choice
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the products list",
            "Add a new product",
            "Update an existing product",
            "Remove an existing product",
            error_func=error_func,
            clear_func=clear_func,
        )
        clear_func()

        # View products
        if Menu_choice == 1:
            list_output_func(prodlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Add a new product
        elif Menu_choice == 2:
            prodlist = new_product_func(prodlist, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Update an existing product
        elif Menu_choice == 3:
            prodlist = update_item_func(
                list_output_func,
                prodlist,
                error_func,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Remove an existing product
        elif Menu_choice == 4:
            prodlist = del_item_func(list_output_func, prodlist, error_func, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Exit to main menu
        elif Menu_choice == 0:
            clear_func()
            break

    # End of product submenu loop


# ---------------------------
# Function: Orders_loop
# Purpose: Display and handle the orders submenu choices including viewing,
#          filtering, adding, updating, and deleting orders.
# Arguments:
#   str_input_func: function to display string menu options
#   error_func: function to validate numeric input
#   list_output_func: function to list raw order entries
#   orderslist: list of order dicts
#   add_order_func: function to add a new order
#   update_existing_order_status_func: function to change order status
#   status_opt_list: list of possible order statuses
#   update_existing_order_func: function to modify order details
#   del_order_func: function to delete an order
#   list_input_func: function to select items and couriers
#   prodlist: list of all products
#   clear_func: function to clear the console screen
#   courlist: list of couriers
#   order_custom_output_function: function to show formatted orders
# ---------------------------
def Orders_loop(
    str_input_func,
    error_func,
    list_output_func,
    orderslist,
    add_order_func,
    update_existing_order_status_func,
    status_opt_list,
    update_existing_order_func,
    del_order_func,
    list_input_func,
    prodlist,
    clear_func,
    courlist,
    order_custom_output_function,
):
    loop1 = 1
    while loop1 == 1:
        clear_func()
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the orders list",
            "view the orders list by assigned courier",
            "view the orders list by status",
            "Add a new order",
            "Update the status of an order",
            "Update an existing order",
            "Remove an existing order",
            error_func=error_func,
            clear_func=clear_func,
        )
        if Menu_choice == 1:
            clear_func()
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
            else:
                clear_func()
                None
        elif Menu_choice == 2:
            order_custom_output_function(
                orderslist,
                2,
                prodlist,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            order_custom_output_function(
                orderslist,
                1,
                prodlist,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 4:
            clear_func()
            orderslist = add_order_func(
                orderslist,
                status_opt_list,
                clear_func,
                list_input_func,
                prodlist,
                error_func,
                courlist,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 5:
            clear_func()
            orderslist = update_existing_order_status_func(
                list_output_func,
                orderslist,
                error_func,
                list_input_func,
                status_opt_list,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 6:
            clear_func()
            orderslist = update_existing_order_func(
                orderslist,
                error_func,
                str_input_func,
                prodlist,
                list_output_func,
                list_input_func,
                clear_func,
                courlist,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 7:
            clear_func()
            orderslist = del_order_func(
                orderslist, list_output_func, error_func, clear_func
            )
            list_output_func(orderslist)
            return_option = rtrn_opt(clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 0:
            clear_func()
            loop1 += 1

    # End of orders submenu loop


# ---------------------------
# Function: courier_loop
# Purpose: Display and handle the couriers submenu choices including viewing,
#          adding, updating, and deleting couriers.
# Arguments:
#   str_input_func: function to display string menu options
#   list_output_func: function to display current couriers
#   courlist: list of courier dicts
#   new_courier_func: function to add a new courier
#   update_courier_func: function to update an existing courier
#   del_courier_func: function to delete a courier
#   error_func: function to validate numeric input
#   clear_func: function to clear the console screen
# ---------------------------
def courier_loop(
    str_input_func,
    list_output_func,
    courlist,
    new_courier_func,
    update_courier_func,
    del_courier_func,
    error_func,
    clear_func,
):
    loop = 1
    while loop == 1:
        clear_func()
        # Show courier menu options and get user's choice
        Menu_choice = str_input_func(
            "Go to the main menu",
            "View the couriers list",
            "Add a new courier",
            "Update an existing courier",
            "Remove an existing courier",
            error_func=error_func,
            clear_func=clear_func,
        )
        clear_func()

        # View couriers
        if Menu_choice == 1:
            list_output_func(courlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Add a new courier
        elif Menu_choice == 2:
            courlist = new_courier_func(courlist, clear_func)
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Update an existing courier
        elif Menu_choice == 3:
            courlist = update_courier_func(
                list_output_func,
                courlist,
                error_func,
                clear_func,
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Remove an existing courier
        elif Menu_choice == 4:
            courlist = del_courier_func(
                list_output_func, courlist, error_func, clear_func
            )
            data.persistence_function(data.products, data.couriers, data.orders)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                clear_func()
                continue

        # Exit to main menu
        elif Menu_choice == 0:
            clear_func()
            break

    # End of couriers submenu loop
