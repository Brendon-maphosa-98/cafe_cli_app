# Print main menu options
def main_menu_opts():
    print("welcome to the main menu, what would you like to do: \n 1: Print Products Menu, \n 2: Print Orders Menu, \n 0: Exit app")

# Print main menu options
def products_menu_opts():
    print("welcome to the products, what would you like to do: \n 1: View all products, \n 2: Add new products, \n 3: Update existing product, \n 4: Delete a product, \n 0: return to main menu")

# Print main menu options
def orders_menu_opts():
    print("welcome to the Orders, what would you like to do: \n 1: Display Orders, \n 2: Create new Order, \n 3: Update Order status, \n 4: Update Existing Order, \n 0: return to main menu")


# create the empty product list for viewing purposes
product_list = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Iced Coffee", "Flat White", "Cold Brew", "Croissant",
 "Blueberry Muffin"]

# create orders menu dictionary data variable

orders = [{'order1': {
    "customer_name": "Alice Smith",
    "customer_address": "High Road, MANCHESTER",
    "customer_phone": "07123456789",
    "status": "ready for pickup",
    "item(s)_ordered": ["Latte", "Blueberry Muffin"]
}},{'order2': {
    "customer_name": "James Carter",
    "customer_address": "Oak Street, LIVERPOOL",
    "customer_phone": "07234567890",
    "status": "preparing",
    "item(s)_ordered": ["Flat White", "Croissant"]
}},{'order3': {
    "customer_name": "Laura Green",
    "customer_address": "Maple Avenue, SHEFFIELD",
    "customer_phone": "07345678901",
    "status": "delivered",
    "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"]
    }}]


# function for add new products to the products data file
def add_product():
    global product_list
    new_product = input("what is the new product you would like to add? ")
    product_list.append(f"{new_product}")

# function for returning list of products from txt file to a list variable here. Not needed in V1 due to no external data source.
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
def print_prod_list():
    print(product_list)   

# function for printing out the up to date orders
def print_orders():
    print(orders)  

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
    first_input = int(input("Input the number corresponding with your desired option > "))
    #while first_input >= 1 : # tested in test enviroment without this while loop and code look's like it works as normal so this is actually not necessery.
    if first_input == 1:
        products_menu_opts()
        prod_menu_input1 = int(input('Select the number associated with your desired option'))
        if prod_menu_input1 == 1:
            print_prod_list()
        elif prod_menu_input1 == 2:
            add_product()
        elif prod_menu_input1 == 3:
            prod_update()
        elif prod_menu_input1 == 4:
            prod_del()
        elif prod_menu_input1 == 0:
            logic_function
    elif first_input == 2:
        orders_menu_opts()
        order_menu_input1 = int(input('\n Select the number associated with your desired option \n'))
        if order_menu_input1 == 1:
            print_orders()
    elif first_input == 0:
        print("you have decided to leave the app, goodbye")
    else: 
        print("Thats not a valid option, try again")
        logic_function()


# app instantiation func 
logic_function()