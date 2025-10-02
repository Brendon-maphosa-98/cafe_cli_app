from src.utils.menu_utils.menu_choice_selection import list_selection_choice

# main menu options that the user can select from

menu_name = "Main"

main_menu_options = ["Orders Menu", "Products Menu", "Couriers Menu", "Exit"]

main_menu_selection = list_selection_choice(
    main_menu_options, f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)

