from src.utils.menu_utils.menu_choice_selection import menu_selection
from src.utils.list_utils.list_view import list_view

menu_name = "Products"

products_main_menu_options = [
    "View Products",
    "Add New Product",
    "Update Existing Product",
    "Delete Product",
    "Return to Main Menu",
]

list_of_products = []

menu_selection(products_main_menu_options)

view_products_list = list_view(list_of_products, menu_name)
