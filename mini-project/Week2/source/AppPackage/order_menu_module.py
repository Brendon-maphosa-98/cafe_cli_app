import re

# Add item function


def add_item(list_input_func, prodlist, error_func, ordernum):
    selected_items = []
    loop = 1
    while loop == 1:
        item_selected = list_input_func(prodlist, error_func)
        option2 = input(
            f"You have selected to add {prodlist[item_selected]} to order{ordernum}\nWould you like to add a another item to the order\n1: Yes\n2: No\n>>> "
        )
        option3 = error_func(option2, 1, 2)
        if option3:
            option2 = int(option2)
            if option2 == 1:
                selected_items.append(prodlist[item_selected])
                loop == 1
            else:
                selected_items.append(prodlist[item_selected])
                print(
                    f"These are the items that have been added to your order ------ {selected_items}"
                )
                loop += 1
                return selected_items
        else:
            print(f"invalid input please try again")

    else:
        return selected_items


# remove item function


def remove_item(
    orderslist,
    error_func,
    remove_order_output_func,
    ordernum,
):
    loop = 1
    selected_items = []
    while loop == 1:
        temp_order_list = orderslist
        print(f"\nBelow are the items currently selected in order{ordernum}\n")
        key = f"order{ordernum}"
        item_selected = remove_order_output_func(
            temp_order_list[ordernum - 1][key]["item(s)_ordered"], error_func
        )
        option2 = input(
            f"You have selected to remove {orderslist[ordernum -1][key]["item(s)_ordered"][item_selected]} from the order\nWould you like to remove another item from the order\n1: Yes\n2: No\n>>> "
        )
        option3 = error_func(option2, 1, 2)
        if option3:
            option2 = int(option2)
            if option2 == 1:
                selected_items.append(
                    temp_order_list[ordernum - 1][key]["item(s)_ordered"][item_selected]
                )
                temp_order_list[ordernum - 1][key]["item(s)_ordered"].remove(
                    temp_order_list[ordernum - 1][key]["item(s)_ordered"][item_selected]
                )

            else:
                selected_items.append(
                    temp_order_list[ordernum - 1][key]["item(s)_ordered"][item_selected]
                )
                temp_order_list[ordernum - 1][key]["item(s)_ordered"].remove(
                    temp_order_list[ordernum - 1][key]["item(s)_ordered"][item_selected]
                )
                print(
                    f"These are the items that have been removed from {key} ------ {selected_items}....confirmed\n"
                )
                return temp_order_list
        else:
            loop == 1


# Add new order function


def add_order(
    cust_fname_str,
    cust_sname_str,
    cust_street_str,
    cust_city_str,
    cust_num_str,
    orderslist,
    status_opt_list,
):

    customer_name1 = input(cust_fname_str)
    customer_name2 = input(cust_sname_str)
    val_loop = 1
    while val_loop == 1:
        customer_address1 = input(cust_street_str)
        customer_address2 = input(cust_city_str)
        if (
            bool(re.search("[0-9]", customer_address1)) == True
            or bool(re.search("[0-9]", customer_address2)) == True
        ):
            print(
                "The delivery street name or city cannot contain any numbers please try again"
            )
            val_loop == 1
        else:
            val_loop += 1
            continue
    val_loop = 1
    while val_loop == 1:
        customer_number = input(cust_num_str)
        if (
            bool(re.search("[a-zA-Z]", customer_number)) == True
            or len(customer_number) != 11
        ):
            print(
                "The customers phone number cannot contain any letters and must be 11 digits long, please try again"
            )
            val_loop == 1
        else:
            val_loop += 1
            continue
    temp_order_list = orderslist
    order = {
        f"order{len(orderslist) + 1}": {
            "customer_name": f"{customer_name1.capitalize()} {customer_name2.capitalize()}",
            "customer_address": f"{customer_address1.title()} {customer_address2.upper()}",
            "customer_phone": customer_number,
            "status": f"{status_opt_list[0]}",
            "item(s)_ordered": [],
        }
    }
    temp_order_list.append(order)
    return temp_order_list


# function for updating an existing order status


def update_existing_order_status(
    dict_output_func,
    orderslist,
    gen_ord_selection_str,
    error_func,
    list_input_func,
    status_opt_list,
):
    loop = 1
    while loop == 1:
        dict_output_func(orderslist)
        chng_sel1 = input(gen_ord_selection_str)
        chng_sel2 = error_func(
            chng_sel1,
            1,
            len(orderslist),
        )
        key = f"order{chng_sel1}"
        if chng_sel2:
            status_chng_sel = list_input_func(status_opt_list, error_func)
            print(
                f"-------You have selected to change the status of order{chng_sel1} from {orderslist[chng_sel1-1][key]["status"]} to {status_opt_list[status_chng_sel]}.......change confirmed-------"
            )
            temp_orders_list = orderslist
            temp_orders_list[chng_sel1 - 1][key]["status"] = status_opt_list[
                status_chng_sel
            ]
            loop += 1
    return temp_orders_list


# update existing order


def update_existing_order(
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
):
    temp_orders_list = orderslist
    loop = 1
    while loop == 1:
        dict_output_func(temp_orders_list)
        chng_sel1 = input(gen_ord_selection_str)
        chng_sel2 = error_func(
            chng_sel1,
            1,
            len(temp_orders_list),
        )
        key = f"order{chng_sel1}"
        if chng_sel2:
            chng_sel1 = int(chng_sel1)
            chng_op1 = str_input_func(
                new_name_str,
                new_address_str,
                new_number_str,
                add_item_str,
                remove_item_str,
                error_func=error_func,
            )
            loop2 = 1
            if chng_op1 == 0:
                customer_name1 = input(new_cust_fname_str)
                customer_name2 = input(new_cust_sname_str)
                print(
                    f"The new customer name for {key} is {customer_name1} {customer_name2} confirmed"
                )
                temp_orders_list[chng_sel1 - 1][key][
                    "customer_name"
                ] = f"{customer_name1.capitalize()} {customer_name2.capitalize()}"
                loop += 1
                return temp_orders_list
            elif chng_op1 == 1:
                while loop2 == 1:
                    customer_address1 = input(new_cust_street_str)
                    customer_address2 = input(new_cust_city_str)
                    if (
                        bool(re.search("[0-9]", customer_address1)) == True
                        or bool(re.search("[0-9]", customer_address2)) == True
                    ):
                        print(
                            "The delivery street name or city cannot contain any numbers please try again"
                        )
                        loop2 == 1
                    else:
                        loop2 += 1
                print(
                    f"The new address for {key} is {customer_address1} {customer_address2} confirmed"
                )
                temp_orders_list[chng_sel1 - 1][key][
                    "customer_address"
                ] = f"{customer_address1.title()} {customer_address2.upper()}"
                loop += 1
                return temp_orders_list
            elif chng_op1 == 2:
                while loop2 == 1:
                    customer_number = input(new_cust_num_str)
                    if (
                        bool(re.search("[a-zA-Z]", customer_number)) == True
                        or len(customer_number) != 11
                    ):
                        print(
                            "The customers phone number cannot contain any letters and must be 11 digits long, please try again"
                        )
                        loop2 == 1
                    else:
                        loop2 += 1
                print(f"The new number for {key} is {customer_number} confirmed")
                temp_orders_list[chng_sel1 - 1][key][
                    "customer_phone"
                ] = f"{customer_number}"
                loop += 1
                return temp_orders_list
            elif chng_op1 == 3:
                for item in add_item(list_input_func, prodlist, error_func, chng_sel1):
                    temp_orders_list[chng_sel1 - 1][key]["item(s)_ordered"].append(item)
                loop += 1
                return temp_orders_list
            elif chng_op1 == 4:
                temp_orders_list = remove_item(
                    temp_orders_list,
                    error_func,
                    remove_order_output_func,
                    ordernum=chng_sel1,
                )
                loop += 1
                return temp_orders_list
            else:
                return temp_orders_list
        else:
            loop == 1
    else:
        return temp_orders_list


# function for deleting an order


def del_order(orderslist, dict_output_func, error_func):
    temp_orders_list = orderslist
    loop = 1
    while loop == 1:
        dict_output_func(temp_orders_list)
        del_input1 = input("Which order from the above would you like to remove?\n>>> ")
        error_check = error_func(del_input1, 1, len(temp_orders_list))
        if error_check:
            del_input1 = int(del_input1)
            print(
                f"You have selected to remove order{del_input1} from the list of orders, this will now be removed.....confirmed\n"
            )
            temp_orders_list.pop(del_input1 - 1)
            loop += 1
            return temp_orders_list
        else:
            print(f"Order{del_input1} does not exist, please try again")
            loop == 1
    return temp_orders_list
