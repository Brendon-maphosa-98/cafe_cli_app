import re

## Courier menu action functions

# function for creating and returning a new product, to be used for adding a new product to the list


def new_courier(courlist, clear_func):
    loop = 1
    while loop == 1:
        clear_func()
        temp_courier_list = courlist
        new_courier_name = input(
            "\nWhat is the name of the courier you would like to add to the list?\n\nNew courier name: "
        )
        new_courier_number = input(
            "\nWhat is the mobile number of the courier you would like to add to the list?\n\nNew courier number: "
        )
        if (
            bool(re.search("[0-9]", new_courier_name)) == True
            or bool(re.search("[a-zA-Z]", new_courier_name)) == False
            or bool(re.search(r"^[a-zA-Z\s\-']+$", new_courier_name)) == False
            or bool(re.search("^[\s]+", new_courier_name)) == True
        ) or (
            bool(re.search("[a-zA-Z]", new_courier_number)) == True
            or len(new_courier_number) != 11
            or bool(re.search("^[\s]+", new_courier_number)) == True
            or new_courier_number[0] != "0"
        ):
            print(
                "Invalid inputs for either your courier name or number\nA courier name must contain letters and cannot contain any numbers or start with a space\nA courier mobile number must not have any letter and only numbers and start with 0 and be 11 digits long\nplease try again"
            )
            loop == 1
        else:
            new_courier = {
                "name": new_courier_name.title(),
                "phone_number": new_courier_number,
            }
            loop += 1
            print(f"\n{new_courier_name.title()} has been added to the couriers list\n")
    temp_courier_list.append(new_courier)
    return temp_courier_list


# function for updating an existing item and returning the new value in the product list


def update_courier(
    list_output_func,
    courlist,
    errorfunc,
    clear_func,
):
    temp_courier_list = courlist
    loop = 1
    while loop == 1:
        list_output_func(temp_courier_list)
        courier_to_remove = input(
            "Which of the above couriers would you like to update?\n>>> "
        )
        valid_rmv_input = errorfunc(courier_to_remove, 1, len(temp_courier_list))
        if valid_rmv_input:
            courier_to_remove = int(courier_to_remove)
            new_courier_name = input(
                "\nWhat is the name of the courier you would like to add in place of the old one?\n\nNew courier name: "
            )
            new_courier_number = input(
                "\nWhat is the mobile number of the courier you would like to add to the list?\n\nNew courier number: "
            )
            if (
                bool(re.search("[0-9]", new_courier_name)) == True
                or bool(re.search("[a-zA-Z]", new_courier_name)) == False
                or bool(re.search(r"^[a-zA-Z\s\-']+$", new_courier_name)) == False
                or bool(re.search("^[\s]+", new_courier_name)) == True
            ) or (
                bool(re.search("[a-zA-Z]", new_courier_number)) == True
                or len(new_courier_number) != 11
                or bool(re.search("^[\s]+", new_courier_number)) == True
                or new_courier_number[0] != "0"
            ):
                print(
                    "Invalid inputs for either your courier name or number\nA courier name must contain letters and cannot contain any numbers or start with a space\nA courier mobile number must not have any letter and only numbers and start with 0 and be 11 digits long\nplease try again"
                )
                loop == 1
            else:
                clear_func()
                courier_to_add = {
                    "name": new_courier_name.title(),
                    "phone_number": new_courier_number,
                }
                print(
                    f"\n{new_courier_name.title()} has been added to the couriers list\n"
                )
                temp_courier_list[courier_to_remove - 1] = courier_to_add
                list_output_func(temp_courier_list)
                loop += 1
                return temp_courier_list
        else:
            loop == 1
            clear_func()


# function for deleting an item and return an updated list


def del_courier(list_output_func, courlist, error_func, clear_func):
    loop = 1
    temp_courier_list = courlist
    while loop == 1:
        list_output_func(temp_courier_list)
        courier_to_remove = input(
            "\nWhich of the above couriers would you like to remove from the list?\n\nInput corresponding number here: "
        )
        valid_rmv_input = error_func(courier_to_remove, 1, len(temp_courier_list))
        if valid_rmv_input:
            clear_func()
            courier_to_remove = int(courier_to_remove)
            print(
                f"{temp_courier_list[courier_to_remove-1]} has been removed from the couriers list"
            )
            temp_courier_list.pop(courier_to_remove - 1)
            list_output_func(temp_courier_list)
            loop += 1
            return temp_courier_list
        else:
            loop == 1
            clear_func()
