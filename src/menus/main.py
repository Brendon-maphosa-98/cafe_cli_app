from src.utils.menu_utils.menu_choice_selection import list_selection_choice

# main menu options that the user can select from

menu_name = "Main"

main_menu_options = {
    1: "Orders Menu",
    2: "Products Menu",
    3: "Couriers Menu",
    0: "Exit",
}

main_menu_selection = list_selection_choice(
    main_menu_options,
    f"Select an option from the {menu_name} menu:",
    allow_zero=True,
)
