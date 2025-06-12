# Print main menu options

def main_menu_opts():
    print("welcome to the main menu, what would you like to do, 1: View all products, 2: Add new products, 3: Update existing product, 4: Delete a product")

# function for add new products to the products data file

def add_product():
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "a") as products:
        new_product = input("what is the new product you would like to add? ")
        products.write(f"{new_product},")

# create the empty product list for viewing purposes

product_list = []

# function for viewing add list of products from txt file to list variable here

def add_to_list():
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/products.txt", "r") as products:
        prod_to_add = products.read().split(",")
        product_list.extend(prod_to_add)

# function for printing out the up to date list of products

def print_list():
    print(product_list)    

# start app
main_menu_opts()
first_input = int(input())
if first_input == 1:
    print_list
elif first_input == 2:
    add_product
# elif first_input == 3:
# elif first_input == 4:
elif first_input == 0:
    print("You have decided to leave the app, till next time")
else: 
    print("Thats not a valid option")