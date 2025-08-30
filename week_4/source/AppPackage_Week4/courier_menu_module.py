import re

# ---------------------------
# Module: Courier Menu Actions
# Provides functions to create, update, and delete courier entries
# within the in-memory courier list.
# ---------------------------


# ---------------------------
# Function: new_courier
# Purpose: Prompt user to enter a new courier name and phone number,
#          validate input, and append the new courier to courlist.
# Arguments:
#   courlist: list of existing courier dicts
#   clear_func: function to clear the console screen
# Returns:
#   Updated courier list including the new courier
# ---------------------------
def new_courier(courlist, clear_func):
    loop = True
    while loop:
        temp_cour_list = courlist
        # Prompt for courier name
        new_courier_name = input(
            "\nWhat is the name of the courier you would like to add to the list?\n\nNew courier name: "
        )
        # Prompt for courier mobile number
        new_courier_number = input(
            "\nWhat is the mobile number of the courier you would like to add to the list?\n\nNew courier number: "
        )

        # Validate name: letters only, no digits, no leading spaces
        invalid_name = (
            bool(re.search(r"[0-9]", new_courier_name))
            or not bool(re.search(r"[a-zA-Z]", new_courier_name))
            or not bool(re.match(r"^[a-zA-Z\s\-']+$", new_courier_name))
            or bool(re.match(r"^\s+", new_courier_name))
        )
        # Validate phone: digits only, length 11, starts with '0', no spaces
        invalid_phone = (
            bool(re.search(r"[a-zA-Z]", new_courier_number))
            or len(new_courier_number) != 11
            or bool(re.match(r"^\s+", new_courier_number))
            or new_courier_number[0] != "0"
        )

        if invalid_name or invalid_phone:
            clear_func()
            print(
                "Invalid inputs for courier name or number:\n"
                "- Name: letters only, cannot start with space\n"
                "- Phone: numeric only, 11 digits, starts with 0\n"
                "Please try again."
            )
        else:
            clear_func()
            # Build new courier dict and append
            new_courier = {
                "name": new_courier_name.title(),
                "phone_number": new_courier_number,
            }
            temp_cour_list.append(new_courier)
            print(f"\n{new_courier['name']} has been added to the couriers list.\n")
            loop = False
    return temp_cour_list


# ---------------------------
# Function: update_courier
# Purpose: Replace an existing courier entry based on user choice.
# Arguments:
#   list_output_func: function to display current couriers
#   courlist: list of existing courier dicts
#   errorfunc: function to validate numeric selection
#   clear_func: function to clear the console screen
# Returns:
#   Updated courier list after replacement
# ---------------------------
def update_courier(list_output_func, courlist, errorfunc, clear_func):
    temp_cour_list = courlist
    while True:
        # Show current couriers with indices
        list_output_func(temp_cour_list)
        choice = input("Which of the above couriers would you like to update?\n>>> ")
        if errorfunc(choice, 1, len(temp_cour_list)):
            idx = int(choice) - 1
            # Prompt for new details
            new_name = input("\nNew courier name: ")
            new_phone = input("\nNew courier number: ")
            # Reuse validation logic
            invalid_name = (
                bool(re.search(r"[0-9]", new_name))
                or not bool(re.search(r"[a-zA-Z]", new_name))
                or not bool(re.match(r"^[a-zA-Z\s\-']+$", new_name))
                or bool(re.match(r"^\s+", new_name))
            )
            invalid_phone = (
                bool(re.search(r"[a-zA-Z]", new_phone))
                or len(new_phone) != 11
                or bool(re.match(r"^\s+", new_phone))
                or new_phone[0] != "0"
            )
            if invalid_name or invalid_phone:
                clear_func()
                print("Invalid name or phone format. Please try again.")
            else:
                clear_func()
                # Update entry in list
                temp_cour_list[idx] = {
                    "name": new_name.title(),
                    "phone_number": new_phone,
                }
                print(f"Courier #{idx+1} updated to {new_name.title()} - {new_phone}\n")
                list_output_func(temp_cour_list)
                return temp_cour_list
        else:
            clear_func()


# ---------------------------
# Function: del_courier
# Purpose: Delete a courier entry based on user selection.
# Arguments:
#   list_output_func: function to display current couriers
#   courlist: list of existing courier dicts
#   error_func: function to validate numeric selection
#   clear_func: function to clear the console screen
# Returns:
#   Updated courier list after deletion
# ---------------------------
def del_courier(list_output_func, courlist, error_func, clear_func):
    temp_cour_list = courlist
    while True:
        # Display current couriers
        list_output_func(temp_cour_list)
        choice = input("\nWhich of the above couriers would you like to remove?\n>>> ")
        if error_func(choice, 1, len(temp_cour_list)):
            idx = int(choice) - 1
            clear_func()
            print(f"{temp_cour_list[idx]['name']} has been removed from the list.\n")
            # Remove and display updated list
            temp_cour_list.pop(idx)
            list_output_func(temp_cour_list)
            return temp_cour_list
        else:
            clear_func()
