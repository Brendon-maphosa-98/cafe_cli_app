# Print main menu options
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
"""def return_frm_txt():
    def nested_return_frm_txt():
        with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "r") as products:
            return products.read().split(",")
    global product_list
    product_list = nested_return_frm_txt()"""

# function for updating existing product
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
        prod_update()

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
    #return_frm_txt()  #return_frm_txt() # Commented out from V1 as data persistance is not possible from what I know without an external data storage file.
    main_menu_opts()
    first_input = int(input())
    while first_input <= 4: # tested in test enviroment without this while loop and code look's like it works as normal so this is actually not necessery.
        if first_input == 1:
            print_list()
            mm_return_func()
        elif first_input == 2:
            add_product()
            #return_frm_txt() # Commented out from V1 as data persistance is not possible from what I know without an external data storage file.
            mm_return_func()
        elif first_input == 3:
            prod_update()
            mm_return_func()
        elif first_input == 4:
            prod_del()
            mm_return_func()    
        elif first_input == 0:
            print("you have decided to leave the app, goodbye")
            break
        else: 
            print("Thats not a valid option, try again")
            logic_function()
        break

# app instantiation func 
logic_function()
