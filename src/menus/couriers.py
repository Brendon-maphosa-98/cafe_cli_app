from src.utils.menu_utils.menu_choice_selection import list_selection_choice

from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_list,
    update_existing_item_in_list,
    delete_item_from_list,
)

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

new_courier = user_prompt_for_new_item(menu_name)

add_new_courier = add_new_item_to_list(menu_name, new_courier, list_of_couriers)

update_courier = update_existing_item_in_list(menu_name, list_of_couriers)

delete_courier = delete_item_from_list(menu_name, list_of_couriers)