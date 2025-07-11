import re

# Add item function


def add_item(list_input_func, prodlist, error_func, ordernum, clear_func):
    selected_items = []
    appending_items = []
    final_items = ""
    loop = 1
    while loop == 1:
        item_selected = list_input_func(prodlist, error_func, clear_func)
        option2 = input(
            f"You have selected to add {prodlist[item_selected]['name']} to order{ordernum}\nWould you like to add a another item to the order\n1: Yes\n2: No\n>>> "
        )
        option3 = error_func(option2, 1, 2)
        if option3:
            option2 = int(option2)
            if option2 == 1:
                selected_items.append(prodlist[item_selected]["name"])
                appending_items.append((prodlist.index(prodlist[item_selected])))
                loop == 1
            else:
                selected_items.append(prodlist[item_selected]["name"])
                appending_items.append((prodlist.index(prodlist[item_selected])))
                print(
                    f"These are the items that have been added to your order ------ {selected_items}"
                )
                loop += 1
                for item in appending_items:
                    final_items += f"{f'{str(item)}, ' if item!=appending_items[-1] else f'{str(item)}'}"
        else:
            print(f"invalid input please try again")

    else:
        return final_items


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
    clear_func,
    list_input_func,
    prodlist,
    error_func,
    courlist,
):
    loop = 1
    clear_func()
    while loop == 1:
        customer_name1 = input(cust_fname_str)
        customer_name2 = input(cust_sname_str)
        if (
            bool(re.search("^[a-zA-Z\s\-]+$", customer_name1)) == False
            or bool(re.search("^[a-zA-Z\s\-]+$", customer_name2)) == False
            or bool(re.search("^[\s]+", customer_name1)) == True
            or bool(re.search("^[\s]+", customer_name2)) == True
        ):
            clear_func()
            print(
                "Customer first or last name are required and can only contain letters or start with a space, please try again\n"
            )
            loop == 1
        else:
            clear_func()
            cust_name_output = f"New customer name will be {customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}\n"
            print(f"{cust_name_output}")
            loop += 1
            continue
    loop = 1
    while loop == 1:
        customer_address1 = input(cust_street_str)
        customer_address2 = input(cust_city_str)
        if (
            bool(re.search("[0-9]", customer_address1)) == True
            or bool(re.search("[0-9]", customer_address2)) == True
            or bool(re.search("^[\s]+", customer_address1)) == True
            or bool(re.search("^[\s]+", customer_address2)) == True
            or bool(re.search(r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~`]", customer_address1))
            == True
            or bool(re.search(r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~`]", customer_address2))
            == True
        ):
            clear_func()
            print(f"{cust_name_output}")
            print(
                "The delivery street name or city are required and cannot contain any numbers, special characters (!@# ect) or start with a space, please try again\n"
            )
            loop == 1
        else:
            clear_func()
            cust_add_output = f"The new customer address will be {customer_address1.title().strip()}, {customer_address2.upper().strip()}\n"
            print(f"{cust_name_output}{cust_add_output}")
            loop += 1
            continue
    loop = 1
    while loop == 1:
        customer_number = input(cust_num_str)
        if (
            bool(re.search("[a-zA-Z]", customer_number)) == True
            or len(customer_number) != 11
            or bool(re.search("^[\s]+", customer_number)) == True
            or customer_number[0] != "0"
        ):
            clear_func()
            print(f"{cust_name_output}{cust_add_output}")
            print(
                "The customers phone number is required and cannot contain any letters or start with a space and must be 11 digits long starting with a zero, please try again\n"
            )
            loop == 1
        else:
            clear_func()
            cust_num_output = (
                f"The customer phone number will be {customer_number.strip()}\n"
            )
            print(f"{cust_name_output}{cust_add_output}{cust_num_output}")
            loop += 1
            continue
    loop = 1
    selected_items = []
    while loop == 1:
        clear_func()
        print("Below are the items currently available to add to the order")
        item_selected = list_input_func(prodlist, error_func, clear_func)
        selected_items.append(prodlist[item_selected - 1])
        more_item = input(
            f"You have selected to add {prodlist[item_selected -1]} to the new order, would you like to add another item?\n1: Yes\n2: No\n>>> "
        )
        more_item_val = error_func(more_item, 1, 2)
        if more_item_val == True and int(more_item) == 1:
            loop == 1
        elif more_item_val == True and int(more_item) == 2:
            loop += 1
            continue
        else:
            loop == 1
    loop = 1
    while loop == 1:
        clear_func()
        print("Below are the Couriers currently available to add to the order")
        courier_selected = list_input_func(courlist, error_func, clear_func)
        print(
            f"You have selected to add {courlist[courier_selected]} as the courier on the new order"
        )
        loop += 1
        continue
    temp_order_list = orderslist
    order = {
        f"order{len(orderslist) + 1}": {
            "customer_name": f"{customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}",
            "customer_address": f"{customer_address1.title().strip()}, {customer_address2.upper().strip()}",
            "customer_phone": customer_number.strip(),
            "status": f"{status_opt_list[0]}",
            "courier": courlist[courier_selected],
            "item(s)_ordered": selected_items,
        }
    }
    temp_order_list.append(order)
    return temp_order_list


# function for updating an existing order status


def update_existing_order_status(
    list_output_func,
    orderslist,
    gen_ord_selection_str,
    error_func,
    list_input_func,
    status_opt_list,
    clear_func,
):
    loop = 1
    while loop == 1:
        clear_func()
        list_output_func(orderslist)
        chng_sel1 = input(gen_ord_selection_str)
        chng_sel2 = error_func(
            chng_sel1,
            1,
            len(orderslist),
        )
        key = f"order{chng_sel1}"
        if chng_sel2:
            chng_sel1 = int(chng_sel1)
            clear_func()
            status_chng_sel = list_input_func(status_opt_list, error_func, clear_func)
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
    clear_func,
    update_courier_str,
    courlist,
):
    temp_orders_list = orderslist
    loop = 1
    clear_func()
    while loop == 1:

        dict_output_func(temp_orders_list)
        chng_sel1 = input(gen_ord_selection_str)
        chng_sel2 = error_func(
            chng_sel1,
            1,
            len(temp_orders_list),
        )
        key = chng_sel1
        clear_func()
        if chng_sel2:
            chng_sel1 = int(chng_sel1)
            chng_op1 = str_input_func(
                new_name_str,
                new_address_str,
                new_number_str,
                add_item_str,
                remove_item_str,
                update_courier_str,
                error_func=error_func,
                clear_func=clear_func,
            )
            loop2 = 1
            clear_func()
            if chng_op1 == 0:
                while loop2 == 1:
                    customer_name1 = input(new_cust_fname_str)
                    customer_name2 = input(new_cust_sname_str)
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
                            f"The new customer name for {key} is {customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}\n"
                        )
                        temp_orders_list[chng_sel1 - 1][key][
                            "customer_name"
                        ] = f"{customer_name1.capitalize().strip()} {customer_name2.capitalize().strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 1:
                while loop2 == 1:
                    customer_address1 = input(new_cust_street_str)
                    customer_address2 = input(new_cust_city_str)
                    if (
                        bool(re.search("[0-9]", customer_address1)) == True
                        or bool(re.search("[0-9]", customer_address2)) == True
                        or bool(re.search("^[\s]+", customer_address1)) == True
                        or bool(re.search("^[\s]+", customer_address1)) == True
                        or bool(
                            re.search(
                                r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~`]", customer_address1
                            )
                        )
                        == True
                        or bool(
                            re.search(
                                r"[!@#$%^*()=+{}\[\]\\|;:\"<>,?~`]", customer_address2
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
                            f"The new address for {key} is {customer_address1.title().strip()}, {customer_address2.upper().strip()} confirmed"
                        )
                        temp_orders_list[chng_sel1 - 1][key][
                            "customer_address"
                        ] = f"{customer_address1.title().strip()}, {customer_address2.upper().strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 2:
                while loop2 == 1:
                    customer_number = input(new_cust_num_str)
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
                            f"The new number for {key} is {customer_number.strip()} confirmed"
                        )
                        temp_orders_list[chng_sel1 - 1][key][
                            "customer_phone"
                        ] = f"{customer_number.strip()}"
                        loop2 += 1
                        loop += 1
                        return temp_orders_list
            elif chng_op1 == 3:
                temp_orders_list[chng_sel1 - 1][chng_sel1]["items"] = add_item(
                    list_input_func, prodlist, error_func, chng_sel1, clear_func
                )
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
            elif chng_op1 == 5:
                temp_orders_list = orderslist
                print(f"Below are the couriers available for order{chng_sel1}:")
                courier_change_selection = list_input_func(
                    courlist, error_func, clear_func
                )
                print(
                    f"You have selected to add {courlist[courier_change_selection]} as the courier for {key}\n"
                )
                temp_orders_list[chng_sel1 - 1][key]["courier"] = courlist[
                    courier_change_selection
                ]
                loop += 1
                return temp_orders_list
        else:
            loop == 1
    else:
        return temp_orders_list


# function for deleting an order


def del_order(orderslist, dict_output_func, error_func, clear_func):
    temp_orders_list = orderslist
    loop = 1
    while loop == 1:
        dict_output_func(temp_orders_list)
        del_input1 = input("Which order from the above would you like to remove?\n>>> ")
        clear_func()
        error_check = error_func(del_input1, 1, len(temp_orders_list))
        if error_check:
            clear_func()
            del_input1 = int(del_input1)
            print(
                f"You have selected to remove order{del_input1} from the list of orders, this will now be removed.....confirmed\n"
            )
            temp_orders_list.pop(del_input1 - 1)
            loop += 1
            return temp_orders_list
        else:
            loop == 1
    return temp_orders_list
