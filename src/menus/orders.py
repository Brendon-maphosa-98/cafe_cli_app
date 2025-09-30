from src.utils.menu_utils.menu_choice_selection import menu_selection
from src.utils.list_utils.list_choice_selection import list_view

menu_name = "Orders"

orders_main_menu_options = [
    "View Orders",
    "Create New Order",
    "Update Existing Order",
    "Delete Order",
    "Return to Main Menu",
]

list_of_orders = []

orders_menu_selection = menu_selection(orders_main_menu_options)

view_orders_list = list_view(list_of_orders, menu_name)
