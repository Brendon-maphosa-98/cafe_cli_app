import data_module as data

# function for printing out lists with index


def list_output(list):
    index_num = 1
    if list == data.PRODUCTS or list == data.order_status:
        print(" ")
        print("-------\n-------")
        for item in list:
            print(f"\n{index_num}. {item}")
            index_num += 1
        print("-------\n-------")
    elif list == data.orders:
        print("")
        for order in list:
            for key, value in order.items():
                print(
                    f"-------\n{key}:\n\nCustomer Name: {value["customer_name"]}\nCustomer Address: {value["customer_address"]}\nContact Number: {value["customer_phone"]}\nStatus: {value["status"]}\nItems: {value["item(s)_ordered"]}\n-------"
                )
    else:
        None


# function for taking and returning inputs


def input_function(*input_str):
    index_num = 0
    for choice in input_str:
        print(f"{index_num}. {choice}")
        index_num += 1
    returned_input = int(
        input("\nWhich of the above options would you like to select?\n")
    )
    return returned_input
