# function to handle choice (menu and lists) selection and validation


def numbered_display(
    options,
    menu_name="options",
):
    """
    Generate a numbered list string from `options` for display.
    Parameters:
      options: A dictionary. The items to be numbered and displayed.
        - For products and couriers this will be a dictionary of items where the key is an item number and the value is the item name. will be provided by the developer.
        - For orders this will be a dictionary of orders where the key is an order number and the value is a dictionary of order details. will be provided by the developer. The last order will NEVER be reserved for 0.
        - For menu options this will be a dictionary of menu options where the key is an option number and the value is the option name. will be provided by the developer.
      menu_name: Name of the menu for display purposes (default is "options").
    Returns:
      A formatted string representing the numbered list, or a message if the list is empty.
    Raises:
        TypeError: if `options` is not a list or dictionary.
    Side Effects:
      - None (pure function).
    Dependencies/Assumptions:
      - `options` is always going to be a dictionary provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
    """
    try:
        if not options:
            return f"No {menu_name} available."
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
      - `user_input` is always going to be a string provided by the user.
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


def list_selection_choice(
    options, prompt_message, menu_name="options"
):
    """
    This function:
    - Displays a numbered list of options to the user.
    - Prompts the user to select an option by entering the corresponding number.
    - Validates the user's input to ensure it corresponds to a valid option.
    - Repeats the prompt until a valid selection is made.
    Parameters:
      options: A dictionary of options where keys are the option numbers (integers) and values are the option names (strings).
      prompt_message: The message displayed to the user when prompting for input.
      menu_name: Name of the menu for display purposes (default is "options").
    Returns:
      The valid user input as a string.
    Raises:
      None (handles invalid input internally).
    Side Effects:
      - Prints the menu and error messages to the console.
      - Waits for user input.
    Dependencies/Assumptions:
      - `options` is always going to be a dictionary provided by the developer.
      - `prompt_message` is always going to be a string provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
      - The keys in `options` are always integers.
      - The function relies on `numbered_display` and `choice_validator` functions.
    """
    function_loop = 0
    while function_loop == 0:
        print(numbered_display(options, menu_name))
        user_input = input(f"\n{prompt_message}\n>>> ")
        selection_output = choice_validator(user_input, options)
        if selection_output == True:
            function_loop = 1
            return user_input
        else:
            print(f"\n{selection_output}\n\n")
