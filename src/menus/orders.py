from src.utils.menu_utils.menu_choice_selection import list_selection_choice
from src.utils.menu_modify_utils.menu_modification import delete_item_from_list

menu_name = "Orders"

orders_main_menu_options = [
    "View Orders",
    "Create New Order",
    "Update Existing Order",
    "Delete Order",
    "Return to Main Menu",
]

list_of_orders = []

orders_menu_selection = list_selection_choice(
    orders_main_menu_options,
    f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)

delete_order = delete_item_from_list(menu_name, list_of_orders)