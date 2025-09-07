import input_output_module as io
import data_module as data
import loops_module as loop
import error_checking_module as error
import product_menu_module as prodmod
import order_menu_module as ordermod
import courier_menu_module as couriermod
import os

# ---------------------------
# Module: Master Loop
# Combines all submenus and drives the main application flow.
# ---------------------------

# ---------------------------
# Function: clear_func
# Purpose: Clear the console screen between menu screens.
# ---------------------------
def clear_func():
    # On UNIX-like systems, 'clear' command clears the terminal
    os.system("clear")
    # Call twice for reliability in some shells
    os.system("clear")


# ---------------------------
# Function: master_loop_function
# Purpose: Initialize data, display the top-level menu,
#          and route to product, courier, or order submenus.
# Workflow:
#   1. Load persisted CSV data into memory (products, couriers, orders)
#   2. Display greeting and main menu repeatedly until user exits
#   3. On selection, invoke the corresponding submenu loop
#   4. On exit choice, persist all data back to CSV and terminate
# ---------------------------
def master_loop_function():
    # Load data into in-memory lists
    data.ingest_function(data.products, data.couriers, data.orders)

    loop_running = True
    while loop_running:
        clear_func()
        # Welcome message and prompt
        print("\n\nHello and welcome to Brendon's coffee shop")
        print("\nHow would you like to proceed? Select from the options below:\n")

        # Display main menu and capture choice
        choice = io.str_input_function(
            "Exit app",
            "Go to the products menu",
            "Go to the couriers menu",
            "Go to the orders menu",
            error_func=error.user_int_check,
            clear_func=clear_func,
        )

        # Route based on user selection
        if choice == 1:
            # Products submenu
            clear_func()
            loop.product_loop(
                str_input_func=io.str_input_function,
                list_output_func=io.list_output,
                prodlist=data.products,
                new_product_func=prodmod.new_product,
                update_item_func=prodmod.update_item,
                del_item_func=prodmod.del_item,
                error_func=error.user_int_check,
                clear_func=clear_func,
            )
        elif choice == 2:
            # Couriers submenu
            clear_func()
            loop.courier_loop(
                str_input_func=io.str_input_function,
                list_output_func=io.list_output,
                courlist=data.couriers,
                new_courier_func=couriermod.new_courier,
                update_courier_func=couriermod.update_courier,
                del_courier_func=couriermod.del_courier,
                error_func=error.user_int_check,
                clear_func=clear_func,
            )
        elif choice == 3:
            # Orders submenu
            clear_func()
            loop.Orders_loop(
                str_input_func=io.str_input_function,
                error_func=error.user_int_check,
                list_output_func=io.list_output,
                orderslist=data.orders,
                add_order_func=ordermod.add_order,
                update_existing_order_status_func=ordermod.update_existing_order_status,
                status_opt_list=data.order_status,
                update_existing_order_func=ordermod.update_existing_order,
                del_order_func=ordermod.del_order,
                list_input_func=io.list_input_function,
                prodlist=data.products,
                clear_func=clear_func,
                courlist=data.couriers,
                order_custom_output_function=io.order_custom_output_function,
            )
        elif choice == 0:
            # Exit: persist data and break main loop
            data.persistence_function(data.products, data.couriers, data.orders)
            clear_func()
            print("\nUntil next time, Bye!\n")
            loop_running = False
        # End of main menu routing

# Entry point
master_loop_function()
