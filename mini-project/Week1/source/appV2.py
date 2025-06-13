# Print main menu options
def main_menu_opts():
    print("welcome to the main menu, what would you like to do, 1: View all products, 2: Add new products, 3: Update existing product, 4: Delete a product, 0: Exit app")


# create the empty product list for viewing purposes
product_list = []

# function for add new products to the products data file
def add_product():
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "a") as products:
        new_product = input("what is the new product you would like to add? ")
        products.write(f"{new_product},")

# function for returning list of products from txt file to a list variable here
def return_frm_txt():
    def nested_return_frm_txt():
        with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "r") as products:
            return products.read().split(",")
    global product_list
    product_list = nested_return_frm_txt()
    product_list.pop(-1)

# function for updating existing product
def prod_update():
    global product_list
    for prod in product_list:
        prodnum = product_list.index(prod) + 1
        print(f"{prodnum} {prod}")
    prod_update_input = int(input("What is the product you would like to update? please give the number associated with the product "))
    update_item = product_list[prod_update_input - 1]
    new_update_val = input((f'You selected {product_list[prod_update_input - 1]}, what would you like to update it to? '))
    product_list[prod_update_input - 1] = new_update_val
    str_var = ""
    for prod in product_list:
        str_var = str_var + f'{prod},'
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "w") as products:
        products.write(str_var)

# function for deleting product

def prod_del():
    return_frm_txt()
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
    str_var = ""
    for prod in product_list:
        str_var = str_var + f'{prod} '
    str_var = str_var.replace(' ', ",")
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "w") as products:
        products.write(str_var)

# function to clean txt file before printing here
#def cleaning_func():


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
    return_frm_txt()
    main_menu_opts()
    first_input = int(input())
    while first_input <= 4: 
        if first_input == 1:
            print_list()
            mm_return_func()
        elif first_input == 2:
            add_product()
            return_frm_txt()
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
