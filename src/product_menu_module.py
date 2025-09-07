import re

# ---------------------------
# Module: Product Menu Actions
# Provides functions to create, update, and delete products
# within the in-memory product list.
# ---------------------------

# ---------------------------
# Function: new_product
# Purpose: Prompt user to enter a new product name and price,
#          validate input, and append the new product to prodlist.
# Arguments:
#   prodlist: list of existing product dicts
#   clear_func: function to clear the console screen
# Returns:
#   Updated product list including the new product
# ---------------------------
def new_product(prodlist, clear_func):
    loop = True
    while loop:
        temp_prod_list = prodlist
        # Ask for product name
        new_prod_name = input(
            "\nWhat is the name of the product you would like to add to the list?\n\nNew product name: "
        )
        # Ask for product price
        new_prod_price = input(
            "\nWhat is the price of the product you would like to add to the list?\n\nNew product price:£"
        )

        # Validate: name must contain letters only, no digits or leading spaces
        # Price must be numeric with optional decimal, no letters or leading spaces
        invalid_name = (
            bool(re.search(r"[0-9]", new_prod_name))
            or not bool(re.search(r"[a-zA-Z]", new_prod_name))
            or not bool(re.match(r"^[a-zA-Z\s\-'.&]+$", new_prod_name))
            or bool(re.match(r"^\s+", new_prod_name))
        )
        invalid_price = (
            bool(re.search(r"[a-zA-Z]", new_prod_price))
            or bool(re.match(r"^\s+", new_prod_price))
            or not bool(re.match(r"^[0-9]+(\.[0-9]+)?$", new_prod_price))
        )

        if invalid_name or invalid_price:
            clear_func()
            print(
                "Invalid inputs for either your product name or price\n"
                "- Name: letters only, no digits, no leading spaces\n"
                "- Price: numeric only, optional decimal point, no letters or spaces\n"
                "Please try again."
            )
        else:
            # Build the new product dict and add to list
            new_prod = {
                "name": new_prod_name.title(),
                "price": float(new_prod_price)
            }
            temp_prod_list.append(new_prod)
            clear_func()
            print(
                f"\n{new_prod['name']} has been added to the products list "
                f"with the price of £{new_prod['price']:.2f}\n"
            )
            loop = False

    return temp_prod_list

# ---------------------------
# Function: update_item
# Purpose: Replace an existing product at a chosen index with a new one.
# Arguments:
#   list_output_func: function to display current products
#   prodlist: list of existing products
#   errorfunc: function to validate numeric selection
#   clear_func: function to clear the console screen
# Returns:
#   Updated product list after replacement
# ---------------------------
def update_item(list_output_func, prodlist, errorfunc, clear_func):
    temp_prod_list = prodlist
    while True:
        clear_func()
        # Show current products with indices
        list_output_func(temp_prod_list)
        choice = input(
            "\nEnter the number of the product you want to replace: "
        )
        if errorfunc(choice, 1, len(temp_prod_list)):
            idx = int(choice) - 1
            # Prompt for replacement details
            new_name = input("\nNew product name: ")
            new_price = input("\nNew product price: £")
            # Validate input using same rules as new_product
            invalid_name = (
                bool(re.search(r"[0-9]", new_name))
                or not bool(re.search(r"[a-zA-Z]", new_name))
                or not bool(re.match(r"^[a-zA-Z\s\-'.&]+$", new_name))
                or bool(re.match(r"^\s+", new_name))
            )
            invalid_price = (
                bool(re.search(r"[a-zA-Z]", new_price))
                or bool(re.match(r"^\s+", new_price))
                or not bool(re.match(r"^[0-9]+(\.[0-9]+)?$", new_price))
            )
            if invalid_name or invalid_price:
                print("Invalid name or price format. Please try again.")
            else:
                clear_func()
                # Update the selected product
                temp_prod_list[idx] = {
                    "name": new_name.title(),
                    "price": float(new_price)
                }
                print(
                    f"Product #{idx+1} updated to "
                    f"{new_name.title()} – £{float(new_price):.2f}\n"
                )
                list_output_func(temp_prod_list)
                return temp_prod_list
        else:
            clear_func()

# ---------------------------
# Function: del_item
# Purpose: Remove a product by index from the product list.
# Arguments:
#   list_output_func: function to display current products
#   prodlist: list of existing products
#   error_func: function to validate numeric selection
#   clear_func: function to clear the console screen
# Returns:
#   Updated product list after deletion
# ---------------------------
def del_item(list_output_func, prodlist, error_func, clear_func):
    temp_prod_list = prodlist
    while True:
        # Show current products
        list_output_func(temp_prod_list)
        choice = input(
            "\nEnter the number of the product you would like to delete: "
        )
        if error_func(choice, 1, len(temp_prod_list)):
            idx = int(choice) - 1
            clear_func()
            print(
                f"{temp_prod_list[idx]['name']} has been removed from the list.\n"
            )
            # Remove the chosen product
            temp_prod_list.pop(idx)
            list_output_func(temp_prod_list)
            return temp_prod_list
        else:
            clear_func()

