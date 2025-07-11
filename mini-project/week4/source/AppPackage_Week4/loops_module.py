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
    Main_menu_str,
    view_option_str,
    create_option_str,
    update_option_str,
    remove_option_str,
    list_output_func,
    prodlist,
    new_product_func,
    created_product_str,
    update_item_func,
    remove_product_str,
    replacement_product_str,
    del_item_func,
    error_func,
    clear_func,
    created_product_price_str,
):
    loop = 1
    while loop == 1:
        clear_func()
        Menu_choice = str_input_func(
            Main_menu_str,
            view_option_str,
            create_option_str,
            update_option_str,
            remove_option_str,
            error_func=error_func,
            clear_func=clear_func,
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
            prodlist = new_product_func(created_product_str, created_product_price_str, prodlist, clear_func)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            clear_func()
            prodlist = update_item_func(
                remove_product_str,
                replacement_product_str,
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
            prodlist = del_item_func(
                remove_product_str, list_output_func, prodlist, error_func, clear_func
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


# Orders loop function


def Orders_loop(
    str_input_func,
    Main_menu_str,
    order_view_option_str,
    order_create_option_str,
    update_status_option_str,
    order_update_option_str,
    order_remove_option_str,
    error_func,
    list_output_func,
    orderslist,
    add_order_func,
    cust_fname_str,
    cust_sname_str,
    cust_street_str,
    cust_city_str,
    cust_num_str,
    update_existing_order_status_func,
    gen_ord_selection_str,
    status_opt_list,
    update_existing_order_func,
    new_name_str,
    new_address_str,
    new_number_str,
    add_item_str,
    remove_item_str,
    new_cust_fname_str,
    new_cust_sname_str,
    new_cust_street_str,
    new_cust_city_str,
    new_cust_num_str,
    del_order_func,
    list_input_func,
    prodlist,
    remove_order_output_func,
    clear_func,
    update_courier_str,
    courlist,
):
    loop1 = 1
    while loop1 == 1:
        clear_func()
        Menu_choice = str_input_func(
            Main_menu_str,
            order_view_option_str,
            order_create_option_str,
            update_status_option_str,
            order_update_option_str,
            order_remove_option_str,
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
            clear_func()
            orderslist = add_order_func(
                cust_fname_str,
                cust_sname_str,
                cust_street_str,
                cust_city_str,
                cust_num_str,
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
        elif Menu_choice == 3:
            clear_func()
            orderslist = update_existing_order_status_func(
                list_output_func,
                orderslist,
                gen_ord_selection_str,
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
        elif Menu_choice == 4:
            clear_func()
            orderslist = update_existing_order_func(
                orderslist,
                gen_ord_selection_str,
                error_func,
                str_input_func,
                new_name_str,
                new_address_str,
                new_number_str,
                add_item_str,
                remove_item_str,
                new_cust_fname_str,
                new_cust_sname_str,
                new_cust_street_str,
                new_cust_city_str,
                new_cust_num_str,
                prodlist,
                list_output_func,
                remove_order_output_func,
                list_input_func,
                clear_func,
                update_courier_str,
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
    Main_menu_str,
    view_courier_option_str,
    create_courier_option_str,
    update_courier_option_str,
    remove_courier_option_str,
    list_output_func,
    courlist,
    new_courier_func,
    created_courier_str,
    update_courier_func,
    remove_courier_str,
    replacement_courier_str,
    del_courier_func,
    error_func,
    clear_func,
):
    loop = 1
    while loop == 1:
        clear_func()
        Menu_choice = str_input_func(
            Main_menu_str,
            view_courier_option_str,
            create_courier_option_str,
            update_courier_option_str,
            remove_courier_option_str,
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
            courlist = new_courier_func(created_courier_str, courlist, clear_func)
            return_option = rtrn_opt(clear_func)
            if return_option == 0:
                loop == 1
                clear_func()
            else:
                None
        elif Menu_choice == 3:
            clear_func()
            courlist = update_courier_func(
                remove_courier_str,
                replacement_courier_str,
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
                remove_courier_str, list_output_func, courlist, error_func, clear_func
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
