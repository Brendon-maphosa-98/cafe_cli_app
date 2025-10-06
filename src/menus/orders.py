from src.utils.menu_utils.menu_choice_selection import (
    list_selection_choice,
    numbered_display,
)

menu_name = "Orders"

orders_main_menu_options = [
    "View Orders",
    "Create New Order",
    "Update Existing Order",
    "Delete Order",
    "Return to Main Menu",
]

dict_of_orders = {}

orders_menu_selection = list_selection_choice(
    orders_main_menu_options,
    f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)

view_orders = numbered_display(dict_of_orders, menu_name)
