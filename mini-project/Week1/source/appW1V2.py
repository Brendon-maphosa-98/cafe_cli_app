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

# input variables to be reused across the script as and when needed
"""
menu_choice = int(input('\nHow would you like to proceed, select from one of the below options\n'))

created_product = input('\n what is the name of the product you would like to add to the list?\n\nNew product name: ')

replaced_product = input('\nwhich of the following products would you like to replace?\n\nInput corresponding number here: ')

replacement_product = input('\n what is the name of the product you would like to add in place of the old one?\n\nNew product name: ')

remove_product = input('\n what is the name of the product you would like to remove from the list?\n\nproduct name: ')

"""

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


options_output(view_option, create_option, update_option, remove_option)
