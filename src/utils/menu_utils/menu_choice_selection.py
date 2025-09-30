# function to validate the users input when selecting menu options


def menu_choice_validator(
    user_input, options
):  # will intake the returned value from the function that takes the users choice.
    try:
        stringint = int(
            user_input
        )  # check that the user input can be turned into an int
        if (
            0 <= stringint < len(options) and len(options) != 0
        ):  # check if that int is less than the length of the options available or 0.
            return True
        elif stringint == 0 and len(options) == 0:
            return True
        else:
            return "NOT_A_VALID_OPTION"
    except ValueError:
        return "NOT_A_NUMBER"


# function used to display menu options across different options


def menu_choices_display(options):
    """
    Build and return a string representation of a numbered menu
    where 0 is always reserved for the 'back' or 'exit' option.
    """

    option_num = 1  # Start numbering at 1 for user-facing menu options
    display_str = ""  # Accumulate the formatted menu into a single string

    for option in options:  # Loop through each option in the list
        if option == options[-1]:
            # Special case: the final option in the list is always assigned to 0
            # (commonly used for "Go Back" or "Exit")
            display_str += f"\n0. {option}"
        else:
            # For all other options, number them sequentially starting at 1
            display_str += f"{option_num}. {option}\n"
            option_num += 1  # Increment the display counter for the next option

    return display_str  # Return the complete formatted menu string


def menu_selection_validator(options, user_input):
    """
    Use menu_choice_validator to validate user input against available options.
    Return the selected option index as an integer if valid,
    or an appropriate error message string if invalid.
    """

    num_of_options = len(options) - 1  # Last valid option index (0-based)
    if menu_choice_validator(user_input, options) == True:
        return user_input
    elif menu_choice_validator(user_input, options) == "NOT_A_VALID_OPTION":
        return f"Please select a valid option between 0 and {num_of_options}"
    elif menu_choice_validator(user_input, options) == "NOT_A_NUMBER":
        return "You must select number"


def menu_selection(options):
    """
    Display a menu of options, prompt the user for input,
    validate the input, and return the selected option index as a string.
    """

    function_loop = 0
    while function_loop == 0:
        print(menu_choices_display(options))
        user_input = input(
            "\nplease select an option from the available options above\n>>> "
        )
        selection_output = menu_selection_validator(options, user_input)
        if selection_output == user_input:
            function_loop = 1
            return selection_output
        else:
            print(f"\n{selection_output}\n\n")


# ====== REFACTOR OF FILE BELOW ======

# generic helpers (core logic)


def numbered_display(
    options, menu_name="options", start_index=1, reserve_zero_for_last=False
):
    """
    Build and return a string representation of a numbered list of options.
    Each option is prefixed with its index in the list, starting from start_index.
    If reserve_zero_for_last is True, the last option is assigned to 0.
    If the options list is empty, return empty_messege or a default message.
    """
    try:
        if not options:
            return "No options to display."
        if len(options) == 0:
            return f"No {menu_name} to display."

        display_str = ""  # Accumulate the formatted list into a single string

        item_index = start_index

        for i, option in enumerate(options):
            if reserve_zero_for_last and i == len(options) - 1:
                display_str += f"\n0. {option.strip()}"
            else:
                display_str += f"{item_index}. {option.strip()}\n"
                item_index += 1

        return (
            display_str.strip().title()
        )  # Return the complete formatted list string without trailing newline
    except Exception as e:
        return f"An error occurred while generating the list: {e}"


def choice_validator(user_input, options, allow_zero=False):
    """
    Validate user input against available options.
    Return the selected option index as an integer if valid,
    or an appropriate error message string if invalid.
    """
    try:
        stringint = int(user_input)
        if allow_zero and stringint == 0 and len(options) != 0:
            return True
        elif 1 <= stringint <= len(options):
            return True
        else:
            return "NOT_A_VALID_OPTION"
    except ValueError:
        return "NOT_A_NUMBER"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def list_selection_choice(options, prompt_message, allow_zero=False, start_index=1, menu_name="options"):
    """
    Display a menu of options, prompt the user for input,
    validate the input, and return the selected option index as a string.
    """
    function_loop = 0
    while function_loop == 0:
        print(numbered_display(options, menu_name,start_index, reserve_zero_for_last=allow_zero))
        user_input = input(f"\n{prompt_message}\n>>> ")
        selection_output = choice_validator(user_input, options, allow_zero=allow_zero)
        if selection_output == True:
            function_loop = 1
            return user_input
        else:
            print(f"\n{selection_output}\n\n")
