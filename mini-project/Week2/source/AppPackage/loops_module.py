# function holding messege for returning to the previous menu


def rtrn_opt():
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
                print(
                    "\nThat is an invalid option, you must enter the number 0, please try again\n"
                )
                loop == 1
        except ValueError:
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
    master_loop_func,
    error_func,
):
    loop = 1
    while loop == 1:

        Menu_choice = str_input_func(
            Main_menu_str,
            view_option_str,
            create_option_str,
            update_option_str,
            remove_option_str,
            error_func=error_func,
        )
        if Menu_choice == 1:
            list_output_func(prodlist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop == 1
            else:
                None
        elif Menu_choice == 2:
            prodlist = new_product_func(created_product_str, prodlist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop == 1
            else:
                None
        elif Menu_choice == 3:
            prodlist = update_item_func(
                remove_product_str,
                replacement_product_str,
                list_output_func,
                prodlist,
                error_func,
            )
            return_option = rtrn_opt()
            if return_option == 0:
                loop == 1
            else:
                None
        elif Menu_choice == 4:
            prodlist = del_item_func(
                remove_product_str, list_output_func, prodlist, error_func
            )
            return_option = rtrn_opt()
            if return_option == 0:
                loop == 1
            else:
                None
        elif Menu_choice == 0:
            print("menu choice option")
            master_loop_func()
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
    dict_output_func,
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
    master_loop_func,
    list_input_func,
    prodlist,
    remove_order_output_func,
):
    loop1 = 1
    while loop1 == 1:
        Menu_choice = str_input_func(
            Main_menu_str,
            order_view_option_str,
            order_create_option_str,
            update_status_option_str,
            order_update_option_str,
            order_remove_option_str,
            error_func=error_func,
        )
        if Menu_choice == 1:
            dict_output_func(orderslist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop1 == 1
            else:
                None
        elif Menu_choice == 2:
            orderslist = add_order_func(
                cust_fname_str,
                cust_sname_str,
                cust_street_str,
                cust_city_str,
                cust_num_str,
                orderslist,
                status_opt_list,
            )
            dict_output_func(orderslist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop1 == 1
            else:
                None
        elif Menu_choice == 3:
            orderslist = update_existing_order_status_func(
                dict_output_func,
                orderslist,
                gen_ord_selection_str,
                error_func,
                list_input_func,
                status_opt_list,
            )
            dict_output_func(orderslist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop1 == 1
            else:
                None
        elif Menu_choice == 4:
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
                dict_output_func,
                remove_order_output_func,
                list_input_func,
            )
            dict_output_func(orderslist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop1 == 1
            else:
                None
        elif Menu_choice == 5:
            orderslist = del_order_func(orderslist, dict_output_func, error_func)
            dict_output_func(orderslist)
            return_option = rtrn_opt()
            if return_option == 0:
                loop1 == 1
            else:
                None
        elif Menu_choice == 0:
            print("menu choice option")
            loop1 += 1
            master_loop_func()
