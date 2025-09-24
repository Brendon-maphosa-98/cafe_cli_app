# function used to display list of items across different menus

def list_view(items, menu_name):
    """
    Build and return a string representation of a numbered list of items.
    Each item is prefixed with its index in the list, starting from 1.
    Assumes that items will be a list of strings.
    Assumes that input items are pre-normalized (e.g., whitespace (trailing and leading)) in an upstream process.
    menu_name will be a string representing the type of items being listed based on the name of the menu i.e. "Couriers", used in the empty list message.
    """
    try:
        if not items:
            return f"No {menu_name} to display."
        if len(menu_name) == 0:
            menu_name = "items"  # Fallback in case of empty menu name

        display_str = ""  # Accumulate the formatted list into a single string

        item_index = 1

        for item in items:  # Start numbering at 1
            if item == "":  # Skip empty strings in the list
                continue
            display_str += f"{item_index}. {item}\n"
            item_index += 1

        return display_str.strip()  # Return the complete formatted list string without trailing newline
    except TypeError:
        return "Invalid input: items or menu name must be a list of strings."