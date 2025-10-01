# function to handle choice (menu and lists) selection and validation

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
        if not isinstance(options, list):
            raise TypeError("Options must be a list.")
        if isinstance(start_index, float) or not isinstance(start_index, int):
            raise TypeError("Start index must be an integer.")
        if not isinstance(reserve_zero_for_last, bool):
            raise TypeError("reserve_zero_for_last must be a boolean.")
        if len(options) == 0:
            return f"No {menu_name} to display."
        if all(option.strip() == "" for option in options):
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
    Validate user input against available options from a numbered list. this is used in conjunction with numbered_display.
    user_input: str - the input provided by the user to validate. It will always be a string.
    options: list - the list of available options to validate against. this will always be a list of strings. will always be provided by developer not user.will always be a list of items or a selection of menu items in the form of a list of strings.
    allow_zero: bool - if True, allows 0 as a valid input for going back or exiting. Default is False. will always be provided by developer not user.
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


def list_selection_choice(
    options, prompt_message, allow_zero=False, start_index=1, menu_name="options"
):
    """
    Display a menu of options, prompt the user for input,
    validate the input, and return the selected option index as a string.
    """
    function_loop = 0
    while function_loop == 0:
        print(
            numbered_display(
                options, menu_name, start_index, reserve_zero_for_last=allow_zero
            )
        )
        user_input = input(f"\n{prompt_message}\n>>> ")
        selection_output = choice_validator(user_input, options, allow_zero=allow_zero)
        if selection_output == True:
            function_loop = 1
            return user_input
        else:
            print(f"\n{selection_output}\n\n")
