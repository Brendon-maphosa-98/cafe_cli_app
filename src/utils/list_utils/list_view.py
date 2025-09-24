# function used to display list of items across different menus

def list_view(items):
    """
    Build and return a string representation of a numbered list of items.
    Each item is prefixed with its index in the list, starting from 1.
    """

    if not items:
        return "No items to display."

    display_str = ""  # Accumulate the formatted list into a single string

    for index, item in enumerate(items, start=1):  # Start numbering at 1
        display_str += f"{index}. {item}\n"

    return display_str.strip()  # Return the complete formatted list string without trailing newline