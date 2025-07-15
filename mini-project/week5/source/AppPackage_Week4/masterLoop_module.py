import input_output_module as io
import data_module as data
import loops_module as loop
import error_checking_module as error
import product_menu_module as prodmod
import order_menu_module as ordermod
import courier_menu_module as couriermod
import os
import re


def clear_func():
    os.system("clear")
    os.system("clear")


# master loop function
def master_loop_function():
    data.ingest_function(data.products, data.couriers, data.orders)
    loop1 = 1
    while loop1 == 1:
        clear_func()
        print("\n\nHello and welcome to Brendon's coffee shop")
        print("\nHow would you like to proceed, select from one of the below options\n")
        choice = io.str_input_function(
            "Exit app\n",
            "Go to the products menu\n",
            "Go to the couriers menu\n",
            "Go to the orders menu\n",
            error_func=error.user_int_check,
            clear_func=clear_func,
        )
        if choice == 1:
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
            loop1 == 1
        elif choice == 2:
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
            loop1 == 1
        elif choice == 3:
            clear_func()
            loop.Orders_loop(
                str_input_func=io.str_input_function,
                error_func=error.user_int_check,
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
                list_output_func=io.list_output,
                order_custom_output_function=io.order_custom_output_function,
            )
            loop1 == 1
        elif choice == 0:
            data.persistence_function(data.products, data.couriers, data.orders)
            clear_func()
            print("\nUntil next time, Bye!\n")
            loop1 += 1
            break

    else:
        clear_func()


#master_loop_function()


def new_product(clear_func):
    loop = 1
    while loop == 1:
        clear_func()
        
        new_prod_name = input(
            "\nWhat is the name of the product you would like to add to the list?\n\nNew product name: "
        )
        new_prod_price = input(
            "\nWhat is the price of the product you would like to add to the list?\n\nNew product price:£"
        )
        if (
            bool(re.search("[0-9]", new_prod_name)) == True
            or bool(re.search("[a-zA-Z]", new_prod_name)) == False
            or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", new_prod_name)) == False
            or bool(re.search("^[\s]+", new_prod_name)) == True
        ) or (
            bool(re.search("[a-zA-Z]", new_prod_price)) == True
            or bool(
                re.search("^[\s]+", new_prod_price) == True
                or bool(re.search(r"^[a-zA-Z\s\-\'\&]+$", new_prod_price)) == True
            )
        ):
            print(
                "Invalid inputs for either your product name or price\nA product name must contain letters and cannot contain any numbers or start with a space\nA product price must not have any letter and only numbers and an optional decimal point\nplease try again"
            )
            loop == 1
        else:
            loop += 1
            print(
                f"\n{new_prod_name.title()} has been added to the products list with the price of £{new_prod_price}\n"
            )
    data.database_send_function('products',new_prod_name.title(),float(new_prod_price))

new_product(clear_func)