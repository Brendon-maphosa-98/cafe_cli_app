import input_output_module as io
import stringVariable_module as stng
import data_module as data
import loops_module as loop
import error_checking_module as error
import product_menu_module as prodmod
import order_menu_module as ordermod


# master loop function
def master_loop_function():

    print("\n\nHello and welcome to Brendon's coffee shop")
    print(stng.menu_choice)
    choice = io.str_input_function(
        stng.exit_app,
        stng.product_menu,
        stng.order_menu,
        error_func=error.user_int_check,
    )
    if choice == 1:
        loop.product_loop(
            str_input_func=io.str_input_function,
            Main_menu_str=stng.Main_menu,
            view_option_str=stng.view_option,
            create_option_str=stng.create_option,
            update_option_str=stng.update_option,
            remove_option_str=stng.remove_option,
            list_output_func=io.list_output,
            prodlist=data.products,
            new_product_func=prodmod.new_product,
            created_product_str=stng.created_product,
            update_item_func=prodmod.update_item,
            remove_product_str=stng.replaced_product,
            replacement_product_str=stng.replacement_product,
            del_item_func=prodmod.del_item,
            master_loop_func=master_loop_function,
            error_func=error.user_int_check,
        )
    elif choice == 2:
        loop.Orders_loop(
            Main_menu_str=stng.Main_menu,
            order_view_option_str=stng.order_view_option,
            order_create_option_str=stng.order_create_option,
            update_status_option_str=stng.update_status_option,
            order_update_option_str=stng.order_update_option,
            order_remove_option_str=stng.order_remove_option,
            str_input_func=io.str_input_function,
            error_func=error.user_int_check,
            orderslist=data.orders,
            add_order_func=ordermod.add_order,
            cust_fname_str=stng.customer_name1,
            cust_sname_str=stng.customer_name2,
            cust_street_str=stng.customer_address1,
            cust_city_str=stng.customer_address2,
            cust_num_str=stng.customer_number,
            update_existing_order_status_func=ordermod.update_existing_order_status,
            gen_ord_selection_str=stng.gen_opt_string,
            status_opt_list=data.order_status,
            update_existing_order_func=ordermod.update_existing_order,
            new_name_str=stng.change_option_customer_name,
            new_address_str=stng.change_option_delivery_address,
            new_number_str=stng.change_option_customer_phone,
            add_item_str=stng.change_option_add_items,
            remove_item_str=stng.change_option_remove_items,
            new_cust_fname_str=stng.customer_name3,
            new_cust_sname_str=stng.customer_name4,
            new_cust_street_str=stng.customer_address3,
            new_cust_city_str=stng.customer_address4,
            new_cust_num_str=stng.customer_number2,
            del_order_func=ordermod.del_order,
            master_loop_func=master_loop_function,
            dict_output_func=io.order_dict_output,
            list_input_func=io.list_input_function,
            prodlist=data.products,
            remove_order_output_func=io.remove_order_output_function,
        )
    elif choice == 0:
        print("\nUntil next time, Bye!\n")
        exit()
    else:
        master_loop_function() and exit()


master_loop_function()

