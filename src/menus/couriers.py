from src.utils.menu_utils.menu_choice_selection import *
from src.utils.menu_modify_utils.menu_modification import user_prompt_for_new_item

menu_name = "Couriers"

couriers_main_menu_options = [
    "View Couriers",
    "Add New Courier",
    "Update Existing Courier",
    "Delete Courier",
    "Return to Main Menu",
]

list_of_couriers = []

courier_menu_selection = menu_selection(couriers_main_menu_options)

view_couriers_list = list_view(list_of_couriers, menu_name)

new_courier = user_prompt_for_new_item(menu_name)