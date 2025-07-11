import data_module as data

# function for printing out lists with index


def list_output(list):
    index_num = 1
    if list == data.products:
        print(" ")
        print("-------\n-------")
        for item in list:
            print(f"\n{index_num}. {item.get('name')} - £{item.get('price')}")
            index_num += 1
        print("-------\n-------")
    elif list == data.couriers:
        print(" ")
        print("-------\n-------")
        for item in list:
            print(f"\n{index_num}. {item.get('name')} - {item.get('phone_number')}")
            index_num += 1
        print("-------\n-------")
    elif list == data.orders:
        for item in list:
            inner_dict = next(iter(item.values()))
            print(
                f'-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nCustomer Address: {inner_dict['customer_address']}\nContact Number: {inner_dict['customer_phone']}\nStatus: {inner_dict['status']}\nCourier: {inner_dict['courier']}\nItems: {inner_dict['items']}\n-------'
            )
            index_num += 1


# functions for taking and returning inputs


def list_input_function(list, error_func, clear_func):
    index_num = 0
    print("-------\n-------")
    loop = 1
    while loop == 1:
        if list == data.products:
            print(" ")
            print("-------\n-------")
            for item in list:
                print(f"\n{index_num}. {item.get('name')} - £{item.get('price')}")
                index_num += 1
            print("-------\n-------")
        elif list == data.couriers:
            print(" ")
            print("-------\n-------")
            for item in list:
                print(f"\n{index_num}. {item.get('name')} - {item.get('phone_number')}")
                index_num += 1
            print("-------\n-------")
        elif list == data.orders:
            for item in list:
                inner_dict = next(iter(item.values()))
                print(
                    f'-------\n{f'Order{index_num}'}:\n\nCustomer Name: {inner_dict['customer_name']}\nCustomer Address: {inner_dict['customer_address']}\nContact Number: {inner_dict['customer_phone']}\nStatus: {inner_dict['status']}\nCourier: {inner_dict['courier']}\nItems: {inner_dict['items']}\n-------'
                )
                index_num += 1
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


def remove_order_output_function(items, error_func):
    index_num = 0
    print("-------\n-------")
    loop = 1
    while loop == 1:
        for item in items:
            print(f"\n{index_num}. {item}")
            index_num += 1
        returned_input = input("\nWhich item above would you like to remove?\n>>> ")
        penultimate_input = error_func(returned_input, 0, len(items) - 1)
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
        clear_func()
        penultimate_input = error_func(returned_input, 0, len(input_str) - 1)
        if penultimate_input:
            final_input = int(returned_input)
            loop += 1
            return final_input
        else:
            loop == 1
            index_num = 0
