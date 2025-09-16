# function used to display menu options across different options
from src.utils.menu_utils.user_input_validation import menu_choice_validator


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
