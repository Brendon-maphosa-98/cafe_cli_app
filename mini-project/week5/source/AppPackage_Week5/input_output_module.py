from itertools import product
import data_module as data


# function for printing out lists with index


def list_output(list):
    index_num = 1
    items_w_names = ""
    if list == "products":
        rows = data.database_fetch_function("products")
        print(" ")
        print("-------\n-------")
        for item in rows:
            print(f"\n{item[0]}. {item[1]} - £{item[2]}")
        print("-------\n-------")
    elif list == "couriers":
        rows = data.database_fetch_function("couriers")
        print(" ")
        print("-------\n-------")
        for item in rows:
            print(f"\n{item[0]}. {item[1]} - {item[2]}")
        print("-------\n-------")
    elif list == data.orders:
        for item in list:
            inner_dict = next(iter(item.values()))
            itemlist = [
                item for item in (inner_dict["items"].replace(",", "").replace(" ", ""))
            ]
            for item in itemlist:
                items_w_names += f"\n{data.products[int(item)]['name']}"
            print(
                f"-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nCustomer Address: {inner_dict['customer_address']}\nContact Number: {inner_dict['customer_phone']}\nStatus: {inner_dict['status']}\nCourier: {data.couriers[int(inner_dict['courier'])]['name']} - {data.couriers[int(inner_dict['courier'])]['phone_number']}\nItems: \n{items_w_names}\n-------"
            )
            items_w_names = ""
            index_num += 1
    elif list == data.order_status:
        print(" ")
        print("-------\n-------")
        for item in list:
            print(f"\n{index_num}. {item}")
            index_num += 1
        print("-------\n-------")


# functions for taking and returning inputs


def list_input_function(list, error_func, clear_func):
    index_num = 0
    items_w_names = ""
    print("-------\n-------")
    loop = 1
    while loop == 1:
        if list == "products":
            rows = data.database_fetch_function("products")
            print(" ")
            print("-------\n-------")
            for item in rows:
                print(f"\n{item[0]}. {item[1]} - £{item[2]}")
            print("-------\n-------")
        elif list == "couriers":
            rows = data.database_fetch_function("couriers")
            print(" ")
            print("-------\n-------")
            for item in rows:
                print(f"\n{item[0]}. {item[1]} - {item[2]}")
        elif list == data.orders:
            for item in list:
                inner_dict = next(iter(item.values()))
                itemlist = [
                    item
                    for item in (inner_dict["items"].replace(",", "").replace(" ", ""))
                ]
                for item in itemlist:
                    items_w_names += f"\n{data.products[int(item)]['name']}"
                print(
                    f"-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nCustomer Address: {inner_dict['customer_address']}\nContact Number: {inner_dict['customer_phone']}\nStatus: {inner_dict['status']}\nCourier: {data.couriers[int(inner_dict['courier'])]['name']} - {data.couriers[int(inner_dict['courier'])]['phone_number']}\nItems: \n{items_w_names}\n-------"
                )
                items_w_names = ""
                index_num += 1
        elif list == data.order_status:
            print(" ")
            print("-------\n-------")
            for item in list:
                print(f"\n{index_num}. {item}")
                index_num += 1
            print("-------\n-------")
        returned_input = input("\nWhich option above would you like to select?\n>>> ")
        clear_func()
        penultimate_input = error_func(returned_input, 0, len(list) - 1)
        if penultimate_input:
            final_input = int(returned_input)
            loop += 1
            return final_input
        else:
            loop == 1
            index_num = 0


def remove_order_output_function(items, products, error_func):
    items = items.replace(",", "").replace(" ", "")
    index_num = 0
    print("-------\n-------")
    loop = 1
    while loop == 1:
        for item in items:
            print(f"\n{index_num}. {products[int(item) -1]['name']}")
            index_num += 1
        returned_input = input("\nWhich item above would you like to remove?\n>>> ")
        penultimate_input = error_func(returned_input, 0, len(products) - 1)
        if penultimate_input:
            final_input = int(returned_input)
            loop += 1
            return final_input
        else:
            loop == 1
            index_num = 0


def str_input_function(*input_str, error_func, clear_func):
    index_num = 0
    print("-------\n-------")
    loop = 1
    while loop == 1:
        for item in input_str:
            print(f"\n{index_num}. {item}")
            index_num += 1
        returned_input = input(
            "\nWhich of the above options would you like to select?\n>>> "
        )
        clear_func
        penultimate_input = error_func(returned_input, 0, len(input_str) - 1)
        if penultimate_input:
            final_input = int(returned_input)
            loop += 1
            return final_input
        else:
            loop == 1
            index_num = 0


def order_custom_output_function(orderslist, view_option, prodlist):
    index_num = 1
    loop = True
    items_w_names = ""
    while loop == True:
        if int(view_option) == 1:
            for order in orderslist:
                inner_dict = next(iter(order.values()))
                itemlist = [
                    item
                    for item in (inner_dict["items"].replace(",", "").replace(" ", ""))
                ]
                for item in itemlist:
                    items_w_names += f"\n{prodlist[int(item)]['name']}"
                print(
                    f"-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nItems: {items_w_names}\nStatus: {(inner_dict['status'])}\n-------"
                )
                items_w_names = ""
                index_num += 1
                loop = False
        elif int(view_option) == 2:
            for order in orderslist:
                inner_dict = next(iter(order.values()))
                itemlist = [
                    item
                    for item in (inner_dict["items"].replace(",", "").replace(" ", ""))
                ]
                for item in itemlist:
                    items_w_names += f"\n{prodlist[int(item)]['name']}"
                print(
                    f"-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nItems: {items_w_names}\nCourier: {data.couriers[int(inner_dict['courier'])]['name']} - {data.couriers[int(inner_dict['courier'])]['phone_number']}\n-------"
                )
                items_w_names = ""
                index_num += 1
                loop = False
