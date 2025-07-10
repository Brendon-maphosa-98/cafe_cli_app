import re

## Courier menu action functions

# function for creating and returning a new product, to be used for adding a new product to the list


def new_courier(created_courier_str, courlist, clear_func):
    loop = 1
    while loop == 1:
        clear_func()
        temp_courier_list = courlist
        new_courier = input(created_courier_str)
        if (
            bool(re.search("[0-9]", new_courier)) == True
            or bool(re.search("[a-zA-Z]", new_courier)) == False
            or bool(re.search(r"^[a-zA-Z\s\-']+$", new_courier)) == False
            or bool(re.search("^[\s]+", new_courier)) == True
        ):
            print(
                "A courier name must contain letters and cannot contain any numbers or start with a space, please try again"
            )
            loop == 1
        else:
            loop += 1
            print(f"\n{new_courier} has been added to the couriers list\n")
    temp_courier_list.append(new_courier)
    return temp_courier_list


# function for updating an existing item and returning the new value in the product list


def update_courier(
    remove_courier_str,
    replacement_courier_str,
    list_output_func,
    courlist,
    errorfunc,
    clear_func,
):
    temp_courier_list = courlist
    loop = 1
    while loop == 1:
        list_output_func(temp_courier_list)
        courier_to_remove = input(remove_courier_str)
        valid_rmv_input = errorfunc(courier_to_remove, 1, len(temp_courier_list))
        if valid_rmv_input:
            courier_to_remove = int(courier_to_remove)
            courier_to_add = input(replacement_courier_str)
            if (
                bool(re.search("[0-9]", courier_to_add)) == True
                or bool(re.search("[a-zA-Z]", courier_to_add)) == False
                or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", courier_to_add)) == False
            ):
                print(
                    "A courier name must contain letters and cannot contain any numbers or start with a space please try again"
                )
                loop == 1
            else:
                clear_func()
                print(
                    f"{courier_to_add} has now replaced {temp_courier_list[courier_to_remove-1]}"
                )
                temp_courier_list[courier_to_remove - 1] = courier_to_add
                list_output_func(temp_courier_list)
                loop += 1
                return temp_courier_list
        else:
            loop == 1
            clear_func()


# function for deleting an item and return an updated list


def del_courier(remove_courier_str, list_output_func, courlist, error_func, clear_func):
    loop = 1
    temp_courier_list = courlist
    while loop == 1:
        list_output_func(temp_courier_list)
        courier_to_remove = input(remove_courier_str)
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
