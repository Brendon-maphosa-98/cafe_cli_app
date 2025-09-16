from art import text2art
from src.utils.menu_utils.menu_choice_selection import (menu_choices_display, menu_selector)

# variable that will hold the letterhead that will be at the top of the main menu

letterhead = text2art("Welcome To Super Cafe")

# main menu options that the user can select from

main_menu_options = ["Orders Menu", "Products Menu", "Couriers Menu", "Exit"]

def main_menu():
    print(letterhead)
    function_loop = 0
    while function_loop == 0:
        print(menu_choices_display(main_menu_options))
        user_input = input("\nplease select an option from the available options above\n>>> ")
        selection_output = menu_selector(main_menu_options,user_input)
        if selection_output == user_input:
            function_loop = 1
            return selection_output
        else:
            print(f'\n{selection_output}\n\n')




