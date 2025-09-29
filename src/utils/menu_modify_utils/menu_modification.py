# functions to add new items to a list

def user_prompt_for_new_item(menu_name, input_fn=input, output_fn=print): 
    """
    Prompt the user to enter a new item name.
    Returns the entered item name as a string, or None if cancelled.
    menu_name: str - the name of the menu (e.g., "items", "couriers")
    """
    try:
        while True:
            new_item = input_fn(f"Enter the name of the new {menu_name[:-1]}: ").strip().title()
            inner_loop = 0
            while inner_loop == 0:
                if not new_item:
                    choice = input_fn("No input provided. Press 1 to try again or 2 to cancel: ")
                    if choice == "2":
                        output_fn(f"Operation cancelled. Returning to {menu_name} menu.")
                        return None
                    elif choice == "1":
                            inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return new_item
    except KeyboardInterrupt:
        output_fn(f"\nOperation cancelled. Returning to {menu_name} menu.")
        return None
    except KeyError:
        output_fn(f"\nEntered key is not recognised. Returning to {menu_name} menu.")
        return None
    except RuntimeError:
        output_fn(f"\nRuntime error occurred. Returning to {menu_name} menu.")
        return None
    except SystemError:
        output_fn(f"\nSystem error occurred. Returning to {menu_name} menu.")
        return None
    except StopIteration:
        output_fn(f"\nNo more input available. Returning to {menu_name} menu.")
        return None
    except Exception as e:
        output_fn(f"\nAn unexpected error occurred: {e}. Returning to {menu_name} menu.")
        return None 
    
