# Core menu items shown on the ordering screen (update only if the menu changes)

PRODUCTS = [
    "Espresso",
    "Cappuccino",
    "Latte",
    "Americano",
    "Mocha",
    "Iced Coffee",
    "Flat White",
    "Cold Brew",
    "Croissant",
    "Blueberry Muffin",
]

## String variables

# string variables to be reused across the script as and when needed

menu_choice = "\nHow would you like to proceed, select from one of the below options\n"

created_product = "\nwhat is the name of the product you would like to add to the list?\n\nNew product name: "

replaced_product = "\nwhich of the above products would you like to replace?\n\nInput corresponding number here: "

replacement_product = "\n what is the name of the product you would like to add in place of the old one?\n\nNew product name: "

remove_product = "\nwhich of the above products would you like to remove from the list?\n\nInput corresponding number here: "

# Variables for the main menu options

Main_menu = "Go to the main menu\n"

product_menu = "Go to the products menu\n"

exit_app = "Exit app\n"

# Variables for the product menu options

view_option = "View the products list\n"

create_option = "Add a new product\n"

update_option = "Update an existing product\n"

remove_option = "Remove an existing product\n"

# function for printing out product list with index


def list_output(product_list):
    index_num = 1
    for product in product_list:
        print(f"\n{index_num}. {product}")
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


# function holding messege for returning to the previous menu
def rtrn_opt():
    rtrn = int(input("-----------------\n\nInput 0 to return to the previous menu\n\n"))
    if rtrn == 0:
        return rtrn
    else:
        print("\nThats an invalid option, please try again\n")
        rtrn_opt()


## app loop functions

# product loop function


def product_loop(products_list):
    Menu_choice = input_function(
        Main_menu, view_option, create_option, update_option, remove_option
    )
    if Menu_choice == 1:
        list_output(products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 2:
        products_list = new_product(created_product, products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 3:
        products_list = update_item(
            remove_product,
            replacement_product,
            list_output(products_list),
            products_list,
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 4:
        products_list = del_item(
            remove_product, list_output(products_list), products_list
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 0:
        master_loop_function(products_list)
    else:
        print("\nInvalid input, try again\n")
        product_loop(products_list)


# master loop function
def master_loop_function(products_list):
    print("\n\nHello and welcome to Brendon's coffee shop")
    print(menu_choice)
    menu_choice = input_function(exit_app, product_menu)
    if menu_choice == 1:
        product_loop(products_list)
    elif menu_choice == 0:
        print("\nUntil next time, Bye!\n")
        exit


master_loop_function(PRODUCTS)
