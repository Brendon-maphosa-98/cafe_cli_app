from src.utils.menu_utils.menu_choice_selection import menu_selection
from src.utils.list_utils.list_view import list_view

menu_name = "Couriers"

couriers_main_menu_options = [
    "View Couriers",
    "Add New Courier",
    "Update Existing Courier",
    "Delete Courier",
    "Return to Main Menu",
]

list_of_couriers = []

menu_selection(couriers_main_menu_options)

view_couriers_list = list_view(list_of_couriers, menu_name)