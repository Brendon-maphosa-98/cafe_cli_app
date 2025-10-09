from src.utils.menu_utils.menu_choice_selection import (
    list_selection_choice,
    numbered_display,
)

from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_collection,
    update_existing_item_in_list,
    delete_item_from_list,
)

menu_name = "Couriers"

# main menu options that the user can select from
couriers_main_menu_options = {
    1: "View Couriers",
    2: "Add New Courier",
    3: "Update Existing Courier",
    4: "Delete Courier",
    0: "Return to Main Menu",
}

dict_of_couriers = {}

courier_menu_selection = list_selection_choice(
    couriers_main_menu_options,
    f"Select an option from the {menu_name} menu:",
)

user_input = input()
view_couriers = numbered_display(dict_of_couriers, menu_name)

menu_display = numbered_display(couriers_main_menu_options, menu_name)

new_courier = user_prompt_for_new_item(menu_name)

add_new_courier = add_new_item_to_collection(new_courier, dict_of_couriers)

update_courier = update_existing_item_in_list(menu_name, dict_of_couriers)

delete_courier = delete_item_from_list(menu_name, user_input, dict_of_couriers)
