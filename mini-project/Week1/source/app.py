import random


# Print main menu options
def main_menu_opts():
    print(
        "welcome to the main menu, what would you like to do: \n 1: Print Products Menu,\n 0: Exit app"
    )


# Print product menu options
def products_menu_opts():
    print(
        "welcome to the products, what would you like to do: \n 1: View all products, \n 2: Add new products, \n 3: Update existing product, \n 4: Delete a product, \n 0: return to main menu"
    )


# create the empty product list for viewing purposes
product_list = [
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


# function for add new products to the products list
def add_product():
    global product_list
    new_product = input("what is the new product you would like to add? ")
    product_list.append(f"{new_product}")


# function for updating existing product
def prod_update():
    for prod in product_list:
        prodnum = product_list.index(prod) + 1
        print(f"{prodnum} {prod}")
    prod_update_input = int(
        input(
            "What is the product you would like to update? please give the number associated with the product "
        )
    )
    if prod_update_input <= len(product_list):
        new_update_val = input(
            (
                f"You selected {product_list[prod_update_input - 1]}, what would you like to update it to? "
            )
        )
        product_list[prod_update_input - 1] = new_update_val
    else:
        print("That's not a valid option please try again")
        prod_update()


# function to delete product


def prod_del():
    for prod in product_list:
        prodnum = product_list.index(prod) + 1
        print(f"{prodnum} {prod}")
    prod_del_input = int(
        input(
            "What is the product you would like to delete? please give the number associated with the product "
        )
    )
    if prod_del_input <= len(product_list):
        del_prod_val = prod_del_input - 1
        print(
            (
                f"You selected {product_list[prod_del_input - 1]}, This will now be removed from the list"
            )
        )
        product_list.pop(del_prod_val)
    else:
        print("That's not a valid option please try again")
        prod_del()


# function for printing out the up to date list of products
def print_prod_list():
    print(product_list)


# main menu return prompt func
def mm_return_func():
    print("Input 0 if you'd like to now return to the main menu")
    mm_return_input = int(input())
    if mm_return_input == 0:
        logic_function()
    else:
        print("Thats not a valid option please try again")
        mm_return_func()


# Base logic func
def logic_function():
    main_menu_opts()
    first_input = int(
        input("Input the number corresponding with your desired option > ")
    )
    if first_input == 1:
        products_menu_opts()
        prod_menu_input1 = int(
            input("Select the number associated with your desired option")
        )
        if prod_menu_input1 == 1:
            print_prod_list()
            mm_return_func()
        elif prod_menu_input1 == 2:
            add_product()
            mm_return_func()
        elif prod_menu_input1 == 3:
            prod_update()
            mm_return_func()
        elif prod_menu_input1 == 4:
            prod_del()
            mm_return_func()
        elif prod_menu_input1 == 0:
            logic_function
    elif first_input == 0:
        print("you have decided to leave the app, goodbye")
    else:
        print("Thats not a valid option, try again")
        logic_function()


# app instantiation func
logic_function()
