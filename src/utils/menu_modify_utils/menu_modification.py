# functions to add new items to a list

def create_new_item():
    """
    Prompt the user to enter a new item name.
    Returns the entered item name as a string.
    """
    loop = 0
    try:
        while loop == 0:
            new_item = input("Enter the name of the new item: ").strip().capitalize()  # Remove leading/trailing whitespace and capitalize
            if not new_item:
                print("No input provided. Please try again.")
            else:
                loop = 1
                return new_item
    except Exception as e:
        return f"An error occurred while creating the item: {str(e)}"