## Product menu action functions

# function for creating and returning a new product, to be used for adding a new product to the list


def new_product(messege, products_list):
    temp_prod_list = products_list
    temp_prod_list.append(input(messege))
    return temp_prod_list


# function for updating an existing item and returning the new value in the product list


def update_item(rmv_product, new_product, list_output, list):
    product_to_remove = int(input(rmv_product))
    print(list_output)
    product_to_add = input(new_product)
    list[product_to_remove - 1] = product_to_add
    return list


# function for deleting an item and return an updated list


def del_item(rmv_str_input, list_output, list):
    item_to_remove = int(input(rmv_str_input))
    print(list_output)
    list.pop(item_to_remove - 1)
    return list
