# function to handle choice (menu and lists) selection and validation


def numbered_display(
    options,
    menu_name="options",
):
    """
    This function:
    - Takes a dictionary of options and a menu name as input.
    - Returns a formatted string displaying the options in a numbered list format.
    Parameters:
      options: A dictionary of options where keys are the valid choices (integers) and values are the option names.
      menu_name: Name of the menu for display purposes (default is "options").
    Returns:
      A formatted string displaying the options in a numbered list format.
    Raises:
      TypeError: if `options` is not a dictionary.
      ValueError: if `options` is empty.
      Exception: for any other unexpected errors.
    Side Effects:
      - None (pure function).
    Dependencies/Assumptions:
      - `options` is always going to be a dictionary provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
      - The keys in `options` are always integers.
      - If `menu_name` is "orders", the values in `options` are expected to be dictionaries with specific keys.
      - If `menu_name` is not "orders", the values in `options` are expected to be strings.
    """
    try:
        if not options:
            raise ValueError
        display_string = f"\n{menu_name.upper()}:\n"
        if menu_name == "orders":
            for key, value in options.items():
                display_string += (
                    f"\nOrder {key}:\n"
                    f"  Customer: {value['customer']}\n"
                    f"  Address: {value['address']}\n"
                    f"  Phone: {value['phone']}\n"
                    f"  Items: {value['items']}\n"
                    f"  Courier: {value['courier']}\n"
                    f"  Status: {value['status']}\n"
                )
        else:
            for key in options:
                display_string += f"\n{key}. {options[key]}\n"
        return display_string
    except TypeError:
        return "Invalid options format. Must be a dictionary."
    except ValueError:
        return f"No {menu_name} available."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def choice_validator(user_input, options):
    """
    This function:
    - Validates if the user input is a valid choice from the provided options.
    Parameters:
      user_input: The input provided by the user (expected to be a string that can be converted to an integer).
      options: A dictionary of valid options where keys are the valid choices (integers).
    Returns:
      True if the input is a valid choice, otherwise an error message string.
    Raises:
      KeyError: if the input number is not a key in `options`.
      ValueError: if the input cannot be converted to an integer.
    Side Effects:
      - None (pure function).
    Dependencies/Assumptions:
      - `user_input` is always going to be a string provided by the user that can be converted to an integer.
      - `options` is always going to be a dictionary provided by the developer.
      - `The keys in `options` are always integers.
    """
    try:
        choice = int(user_input)
        if choice in options.keys():
            return True
        else:
            raise KeyError
    except KeyError:
        return f"Invalid choice. Please select a valid option from the list."
    except ValueError:
        return "Invalid input. Please enter a number."


def list_selection_choice(options, user_input, menu_name="options"):
    """
    This function:
    - Displays a numbered list of options.
    - validates user input against the options.
    - Returns the valid user input.
    Parameters:
      options: A dictionary of options where keys are the valid choices (integers) and values are the option names.
      user_input: The input provided by the user (expected to be a variable containing a string that can be converted to an integer).
      menu_name: Name of the menu for display purposes (default is "options").
    Returns:
      The valid user input (as a string) if it is a valid choice from the options, otherwise None.
    Raises:
      None (handles exceptions internally).
    Side Effects:
      - Prints the numbered list and error messages to the console.
    Dependencies/Assumptions:
      - `options` is always going to be a dictionary provided by the developer.
      - `user_input` is always going to be a variable containing a string provided by the user. the variable is passed to the function by the developer.
      - `menu_name` is always going to be a string provided by the developer.
      - The keys in `options` are always integers.
    """
    # TODO: refactor to give user option to cancel selection and return to previous menu
    try:
        is_running = True
        while is_running:
            print(numbered_display(options, menu_name))
            selection_output = choice_validator(user_input, options)
            if selection_output == True:
                is_running = False
                return user_input
            else:
                print(selection_output)
                is_running = True
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
