import re


## Product menu action functions

# function for creating and returning a new product, to be used for adding a new product to the list


def new_product(prodlist, clear_func):
    loop = 1
    while loop == 1:
        clear_func()
        temp_prod_list = prodlist
        new_prod_name = input(
            "\nWhat is the name of the product you would like to add to the list?\n\nNew product name: "
        )
        new_prod_price = input(
            "\nWhat is the price of the product you would like to add to the list?\n\nNew product price:£"
        )
        if (
            bool(re.search("[0-9]", new_prod_name)) == True
            or bool(re.search("[a-zA-Z]", new_prod_name)) == False
            or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", new_prod_name)) == False
            or bool(re.search("^[\s]+", new_prod_name)) == True
        ) or (
            bool(re.search("[a-zA-Z]", new_prod_price)) == True
            or bool(
                re.search("^[\s]+", new_prod_price) == True
                or bool(re.search(r"^[a-zA-Z\s\-\'\&]+$", new_prod_price)) == True
            )
        ):
            print(
                "Invalid inputs for either your product name or price\nA product name must contain letters and cannot contain any numbers or start with a space\nA product price must not have any letter and only numbers and an optional decimal point\nplease try again"
            )
            loop == 1
        else:
            new_prod = {"name": new_prod_name.title(), "price": float(new_prod_price)}
            loop += 1
            print(
                f"\n{new_prod_name.title()} has been added to the products list with the price of £{new_prod_price}\n"
            )
    temp_prod_list.append(new_prod)
    return temp_prod_list


# function for updating an existing item and returning the new value in the product list


def update_item(
    list_output_func,
    prodlist,
    errorfunc,
    clear_func,
):
    temp_prod_list = prodlist
    loop = 1
    while loop == 1:
        clear_func()
        list_output_func(temp_prod_list)
        product_to_remove = input(
            "\nWhich of the above products would you like to remove from the list?\n\nInput corresponding number here: "
        )
        valid_rmv_input = errorfunc(product_to_remove, 1, len(temp_prod_list))
        if valid_rmv_input:
            product_to_remove = int(product_to_remove)
            product_to_add_name = input(
                "\nWhat is the name of the product you would like to add in place of the old one?\n\nNew product name: "
            )
            product_to_add_price = input(
                "\nWhat is the price of the product you would like to add in place of the old one?\n\nNew product price:£"
            )
            if (
                bool(re.search("[0-9]", product_to_add_name)) == True
                or bool(re.search("[a-zA-Z]", product_to_add_name)) == False
                or bool(re.search(r"^[a-zA-Z\s\-'\.&]+$", product_to_add_name)) == False
                or bool(re.search("^[\s]+", product_to_add_name)) == True
            ) or (
                bool(re.search("[a-zA-Z]", product_to_add_price)) == True
                or bool(
                    re.search("^[\s]+", product_to_add_price) == True
                    or bool(re.search(r"^[a-zA-Z\s\-\'\&]+$", product_to_add_price))
                    == True
                )
            ):
                print(
                    "Invalid inputs for either your product name or price\nA product name must contain letters and cannot contain any numbers or start with a space\nA product price must not have any letter and only numbers and an optional decimal point\nplease try again"
                )
                loop == 1
            else:
                clear_func()
                product_to_add = {
                    "name": product_to_add_name.title(),
                    "price": float(product_to_add_price),
                }
                print(
                    f"{product_to_add_name.title()} has now been added to the product list with a price of £{product_to_add_price}\n"
                )
                temp_prod_list[product_to_remove - 1] = product_to_add
                list_output_func(temp_prod_list)
                loop += 1
                return temp_prod_list
        else:
            loop == 1
            clear_func()


# function for deleting an item and return an updated list


def del_item(list_output_func, prodlist, error_func, clear_func):
    loop = 1
    temp_prod_list = prodlist
    while loop == 1:
        list_output_func(temp_prod_list)
        item_to_remove = input(
            "\nWhich of the above products would you like to remove from the list?\n\nInput corresponding number here: "
        )
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
