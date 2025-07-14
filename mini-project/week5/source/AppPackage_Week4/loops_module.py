# function holding messege for returning to the previous menu


def rtrn_opt(clear_func):
    loop = 1
    while loop == 1:
        try:
            rtrn = int(
                input("-----------------\n\nInput 0 to return to the previous menu\n\n")
            )
            if rtrn == 0:
                loop += 1
                return rtrn
            else:
                clear_func()
                print(
                    "\nThat is an invalid option, you must enter the number 0, please try again\n"
                )
                loop == 1
        except ValueError:
            clear_func()
            print(
                f"You entered an invalid input, you must enter the number 0, please try again\n"
            )
            loop == 1


# product loop function
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
    loop = 1
    while loop == 1:
        clear_func()
        Menu_choice = str_input_func(
           "Go to the main menu\n",
            "View the products list\n",
            "Add a new product\n",
            "Update an existing product\n",
            "Remove an existing product\n",
            error_func=error_func,
            clear_func=clear_func(),
        )
        clear_func()
        if Menu_choice == 1:
            clear_func()
            list_output_func(prodlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 2:
            clear_func()
            prodlist = new_product_func(prodlist, clear_func)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            clear_func()
            prodlist = update_item_func(
                list_output_func,
                prodlist,
                error_func,
                clear_func,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 4:
            clear_func()
            prodlist = del_item_func(list_output_func, prodlist, error_func, clear_func)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 0:
            clear_func()
            loop += 1
    else:
        loop == 1


# Orders loop function


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
            "Go to the main menu\n",
            "View the orders list\n",
            "view the orders list by assigned courier\n",
            "view the orders list by status\n",
            "Add a new order\n",
            "Update the status of an order\n",
            "Update an existing order\n",
            "Remove an existing order\n",
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
            order_custom_output_function(orderslist, 2, prodlist,)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            order_custom_output_function(orderslist, 1, prodlist,)
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
            if return_option == 0:
                loop1 == 1
                clear_func()
            else:
                None
        elif Menu_choice == 0:
            clear_func()
            loop1 += 1


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
        Menu_choice = str_input_func(
            "Go to the main menu\n",
            "View the couriers list\n",
            "Add a new courier\n",
            "Update an existing courier\n",
            "Remove an existing courier\n",
            error_func=error_func,
            clear_func=clear_func,
        )
        clear_func()
        if Menu_choice == 1:
            clear_func()
            list_output_func(courlist)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 2:
            clear_func()
            courlist = new_courier_func(
                courlist,
                clear_func,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            clear_func()
            courlist = update_courier_func(
                list_output_func,
                courlist,
                error_func,
                clear_func,
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 4:
            clear_func()
            courlist = del_courier_func(
                list_output_func, courlist, error_func, clear_func
            )
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 0:
            clear_func()
            loop += 1
    else:
        loop == 1
