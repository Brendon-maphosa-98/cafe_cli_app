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

# string variables to be reused across the script as and when needed

menu_choice = "\nHow would you like to proceed, select from one of the below options\n"

created_product = "\nwhat is the name of the product you would like to add to the list?\n\nNew product name: "

replaced_product = "\nwhich of the following products would you like to replace?\n\nInput corresponding number here: "

replacement_product = "\n what is the name of the product you would like to add in place of the old one?\n\nNew product name: "

remove_product = "\n what is the name of the product you would like to remove from the list?\n\nproduct name: "

# Variables for the main menu options

product_menu = "Go to the products menu\n"

# Variables for the product menu options

view_option = "View the products list\n"

create_option = "Add a new product\n"

update_option = "Update an existing product\n"

remove_option = "Remove an existing product\n"

# function for outputing options to the terminal


def options_output(*options_output):
    index_num = 1
    for option in options_output:
        print(f"{index_num}. {option}")
        index_num += 1


# function for printing out product list with index


def list_output(product_list):
    index_num = 1
    for product in product_list:
        print(f"\n{index_num}. {product}")
        index_num += 1


# function for taking and returning inputs


def input_function(*input_str):
    for choice in input_str:
        returned_input = input(choice)
    return returned_input


# function for creating and returning a new product, to be used for adding a new product to the list


def new_product(input):
    return input


# function for updating an existing item and returning the new value


def update_item(rmv_product, new_product, list_output, list):
    product_to_remove = int(input(rmv_product))
    print(list_output)
    product_to_add = input(new_product)
    list[product_to_remove - 1] = product_to_add
    return list


products = update_item(
    replaced_product, replacement_product, list_output(PRODUCTS), PRODUCTS
)

print(PRODUCTS)
