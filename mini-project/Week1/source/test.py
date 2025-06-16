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