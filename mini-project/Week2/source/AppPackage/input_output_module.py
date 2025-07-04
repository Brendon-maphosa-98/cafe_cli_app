# function for printing out lists with index


def list_output(list):
    index_num = 1
    for item in list:
        print(f"\n{index_num}. {item}")
        index_num += 1


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
