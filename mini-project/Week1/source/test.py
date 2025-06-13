"""list_var = []

def add_to_list():
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/test.txt", "r") as test:
        return test.read().split(",")

list_var = add_to_list()

print(list_var)

test_list = ["Mocha","tea","coffee"]

#def print_prod_names():
    #for item in test_list:
        #print(f"{} {item}")

def testfunc():
    for item in test_list:
        itemnum = test_list.index(f"{item}") + 1
        print(f"{itemnum} {item}")

testfunc()"""

"""# Print main menu options
def main_menu_opts():
    print("welcome to the main menu, what would you like to do, 1: View all products, 2: Add new products, 3: Update existing product, 4: Delete a product, 0: Exit app")


# create the empty product list for viewing purposes
product_list = []

# function for add new products to the products data file
def add_product():
    global product_list
    new_product = input("what is the new product you would like to add? ")
    product_list.append(f"{new_product}")

# function for returning list of products from txt file to a list variable here
def return_frm_txt():
    def nested_return_frm_txt():
        with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "r") as products:
            return products.read().split(",")
    global product_list
    product_list = nested_return_frm_txt()"""

"""# function for updating existing product
def prod_update():
    for prod in product_list:
        prodnum = product_list.index(prod) + 1
        print(f"{prodnum} {prod}")
    prod_update_input = int(input("What is the product you would like to update? please give the number associated with the product "))
    if prod_update_input <= len(product_list):
        new_update_val = input((f'You selected {product_list[prod_update_input - 1]}, what would you like to update it to? '))
        product_list[prod_update_input - 1] = (new_update_val)
    else:
        print("That's not a valid option please try again")
        prod_del()

# function to delete product

def prod_del():
    for prod in product_list:
        prodnum = product_list.index(prod) + 1
        print(f"{prodnum} {prod}")
    prod_del_input = int(input("What is the product you would like to delete? please give the number associated with the product "))
    if prod_del_input <= len(product_list):
        del_prod_val = prod_del_input - 1
        print((f'You selected {product_list[prod_del_input - 1]}, This will now be removed from the list'))
        product_list.pop(del_prod_val)
    else:
        print("That's not a valid option please try again")
        prod_del()

# function for printing out the up to date list of products
def print_list():
    print(product_list)   

# function for input prompt
def input_prompt():
    first_input = int(input())

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
    #return_frm_txt()  # Commented out from V1 as it is now redundant to update product list at the top of the loop as here the product list is not external from the .py file.
    main_menu_opts()
    first_input = int(input())
    if first_input == 1:
        print_list()
        mm_return_func()
    elif first_input == 2:
        add_product()
        #return_frm_txt() # Commented out from V1 as it is now redundant to update product list after added a product as here the product list is not external from the .py file as this is done automatically.
        mm_return_func()
    elif first_input == 3:
        prod_update()
        mm_return_func()
    elif first_input == 4:
        prod_del()
        mm_return_func()    
    elif first_input == 0:
        print("you have decided to leave the app, goodbye")
    else: 
        print("Thats not a valid option, try again")
        logic_function()

# app instantiation func 
logic_function()"""


"""product_list = ['mocha','cheese','sandwhich','tea']

str_var = str(product_list)
#str_var.strip()
str_var.replace("[", " ")
#str_var.replace("[", "")
#str_var.replace("]", "")
#str_var.replace("'", "")

new_var = ""
for x in product_list:
    new_var = new_var + f'{x},'

new_var = new_var.title()

print(new_var)"""

"""product_list = []

def return_frm_txt():
    def nested_return_frm_txt():
        with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/test.txt", "r") as products:
            return products.read().split(",")
    global product_list
    product_list = nested_return_frm_txt()
    #product_list.pop(-1)

return_frm_txt()
print(product_list)"""

import os
import time

# Predifined products list
products = ["mocha", "americano", "flat white", "latte"]


# Print the product list. 
# Option: 0 - display indexes and product names, 1 - display numbering from 1 and product names.
def print_products(products: list, option: int):
    print("\n== Product list: ==")
    for idx, product in enumerate(products):
        print(f"{idx+option}. {product}".title())


# Add new product to the product list.
def add_product(new_product: str, products: list):
    product = new_product.lower()

    if product not in products:
        products.append(product)
        print(f"Product '{product}' was successfully added to the product list.")
    else:
        print(f"Product '{product}' wasn't added. It is already in the product list.")


# Update product name by index.
def update_product_by_idx(product_idx: int, new_product: str, products: list):
    if product_idx >= 0 and product_idx < len(products):
        old_product = products[product_idx]
        products[product_idx] = new_product.lower()
        print(
            f"Product with index [{product_idx}] - '{old_product}' - was successfully changed to '{new_product.lower()}'."
        )
    else:
        print(f"Product index [{product_idx}] is out of product list range.")


# Delete product by index.
def del_product_by_index(product_idx: int, products: list):
    if product_idx >= 0 and product_idx < len(products):
        product = products[product_idx]
        chioce=input(f"Are you sure you want to delete '{product}' from product list? [y/n]:")
        if chioce.lower()=='y':
            del products[product_idx]
            print(
                f"Product with index [{product_idx}] - '{product}' - was successfully removed from product list."
            )
        else:
            print("Deletion has been canceled.")
    else:
        print(
            f"Product index [{product_idx}] is out of product list range."
        )


# Clear screen function.
def clear_screen():
    #This solution will not clear screen properly, it will leave opportunity to scroll back.
    os.system('cls' if os.name == 'nt' else 'clear')
    # This solution will clean screen properly, but it looks strange.
    #print("\033c\033[3J")


# Validate input and ask for new untill get value int>0.
def return_int_input(message:str):
    while True:
        user_input = input(message)
        if user_input.isnumeric(): 
            indx = int(user_input)
            break
        else:
            print("Invalid index.")
    return indx


# Main menu interface: handles main menu navigation and user actions.
def main_menu():
    while True:
        clear_screen()
        print("\n===== Main Menu =====")
        print("0. EXIT")
        print("1. View PRODUCT MENU options")

        choice = input("\nSelect an option: ")

        if choice == "0":
            print("Exiting the main menu.")
            return #change to break?
        elif choice == "1":
            product_menu()
        else:
            print("\nInvalid choice. Please try again.")


# Product menu interface: handles product menu navigation and user actions.
def product_menu():
    clear_screen()
    print("\n===== Product Menu =====")
    print("0. RETURN to main menu")
    print("1. PRINT products list")
    print("2. CREATE new product")
    print("3. UPDATE existing product")
    print("4. DELETE product")

    while True:
        choice = input("\nSelect an option from product menu: ")

        if choice == "0":
            return

        elif choice == "1":
            print_products(products, 1)
            time.sleep(3)

        elif choice == "2":
            while True:
                product = input("Enter the product name: ")
                add_product(product, products)

                choice = input(
                    "Would you like to add one more product to the product list? [y/n]: "
                ).lower()
                if choice != "y":
                    break

        elif choice == "3":
            print_products(products, 0)
            indx=return_int_input("Enter an index for product you would like to update: ")
            product = input("Enter new product name: ")
            update_product_by_idx(indx, product, products)

        elif choice == "4":
            print_products(products, 0)
            indx = return_int_input("Enter an index for product you would like to delete: ")
            del_product_by_index(indx, products)
        else:
            print("\nInvalid choice. Please try again.")


#Main program
main_menu()
