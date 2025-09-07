import re

## Product menu action functions

# function for creating and returning a new product, to be used for adding a new product to the list


def new_product(created_product_str, prodlist, clear_func):
    loop = 1
    while loop == 1:
        clear_func()
        temp_prod_list = prodlist
        new_prod = input(created_product_str)
        if (
            bool(re.search("[0-9]", new_prod)) == True
            or bool(re.search("[a-zA-Z]", new_prod)) == False
            or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", new_prod)) == False
        ):
            print(
                "A product name must contain letters and cannot contain any numbers please try again"
            )
            loop == 1
        else:
            loop += 1
            print(f"\n{new_prod} has been added to the products list\n")
    temp_prod_list.append(new_prod)
    return temp_prod_list


# function for updating an existing item and returning the new value in the product list


def update_item(
    remove_product_str,
    replacement_product_str,
    list_output_func,
    prodlist,
    errorfunc,
    clear_func,
):
    temp_prod_list = prodlist
    loop = 1
    while loop == 1:
        list_output_func(temp_prod_list)
        product_to_remove = input(remove_product_str)
        valid_rmv_input = errorfunc(product_to_remove, 1, len(temp_prod_list))
        if valid_rmv_input:
            product_to_remove = int(product_to_remove)
            product_to_add = input(replacement_product_str)
            if (
                bool(re.search("[0-9]", product_to_add)) == True
                or bool(re.search("[a-zA-Z]", product_to_add)) == False
                or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", product_to_add)) == False
            ):
                print(
                    "A product name must contain letters and cannot contain any numbers please try again"
                )
                loop == 1
            else:
                clear_func()
                print(
                    f"{product_to_add} has now replaced {temp_prod_list[product_to_remove-1]}"
                )
                temp_prod_list[product_to_remove - 1] = product_to_add
                list_output_func(temp_prod_list)
                loop += 1
                return temp_prod_list
        else:
            loop == 1
            clear_func()


# function for deleting an item and return an updated list


def del_item(remove_product_str, list_output_func, prodlist, error_func, clear_func):
    loop = 1
    temp_prod_list = prodlist
    while loop == 1:
        list_output_func(temp_prod_list)
        item_to_remove = input(remove_product_str)
        valid_rmv_input = error_func(item_to_remove, 1, len(temp_prod_list))
        if valid_rmv_input:
            clear_func()
            item_to_remove = int(item_to_remove)
            print(
                f"{temp_prod_list[item_to_remove-1]} has been removed from the products list"
            )
            temp_prod_list.pop(item_to_remove - 1)
            list_output_func(temp_prod_list)
            loop += 1
            return temp_prod_list
        else:
            loop == 1
            clear_func()
