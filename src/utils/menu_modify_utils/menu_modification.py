# functions to add new items to a list

def user_prompt_for_new_item(menu_name, input_fn=input, output_fn=print): 
    """
    Prompt the user to enter a new item name.
    Returns the entered item name as a string, or None if cancelled.
    menu_name: str - the name of the menu (e.g., "items", "couriers")
    """
    while True:
        new_item = input_fn(f"Enter the name of the new {menu_name[:-1]}: ").strip()
        if not new_item:
            choice = input_fn("No input provided. Press 1 to try again or 2 to cancel: ")
            if choice == "2":
                output_fn(f"Operation cancelled. Returning to {menu_name} menu.")
                return None
        else:
            return new_item
    
