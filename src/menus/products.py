from src.utils.menu_utils.menu_choice_selection import (
    list_selection_choice,
    numbered_display,
)


from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_list,
    update_existing_item_in_list,
    delete_item_from_list,
)

menu_name = "Products"

products_main_menu_options = [
    "View Products",
    "Add New Product",
    "Update Existing Product",
    "Delete Product",
    "Return to Main Menu",
]

list_of_products = []

products_menu_selection = list_selection_choice(
    products_main_menu_options,
    f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)

view_products = numbered_display(list_of_products, menu_name)

new_product = user_prompt_for_new_item(menu_name)

add_new_product = add_new_item_to_list(menu_name, new_product, list_of_products)

update_product = update_existing_item_in_list(menu_name, list_of_products)

delete_product = delete_item_from_list(menu_name, list_of_products)
