from src.utils.menu_utils.menu_choice_selection import menu_selection
from src.utils.list_utils.list_choice_selection import list_view
from src.utils.menu_modify_utils.menu_modification import user_prompt_for_new_item

menu_name = "Products"

products_main_menu_options = [
    "View Products",
    "Add New Product",
    "Update Existing Product",
    "Delete Product",
    "Return to Main Menu",
]

list_of_products = []

products_menu_selection = menu_selection(products_main_menu_options)

view_products_list = list_view(list_of_products, menu_name)

new_product = user_prompt_for_new_item(menu_name)

