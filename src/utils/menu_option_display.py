# function used to display menu options across different options


def menu_choice_display(options):
    """
    Build and return a string representation of a numbered menu
    where 0 is always reserved for the 'back' or 'exit' option.
    """

    option_num = 1               # Start numbering at 1 for user-facing menu options
    display_str = ""             # Accumulate the formatted menu into a single string

    for option in options:       # Loop through each option in the list
        if option == options[-1]:
            # Special case: the final option in the list is always assigned to 0
            # (commonly used for "Go Back" or "Exit")
            display_str += f"\n0. {option}"
        else:
            # For all other options, number them sequentially starting at 1
            display_str += f"{option_num}. {option}\n"
            option_num += 1      # Increment the display counter for the next option

    return display_str           # Return the complete formatted menu string
