from src.utils.menu_utils.menu_choice_selection import (
    list_selection_choice,
    numbered_display,
)
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

courier_menu_selection = list_selection_choice(
    couriers_main_menu_options,
    f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)

view_couriers_list = numbered_display(list_of_couriers, menu_name)

new_courier = user_prompt_for_new_item(menu_name)
