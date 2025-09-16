# test_menu_choice_display.py

from src.utils.menu_option_display import menu_choice_display


def test_three_options_menu():
    # options = ["Add", "View", "Exit"]
    # Expected:
    # 1. Add
    # 2. View
    #
    # 0. Exit
    options = ["Add", "View", "Exit"]
    expected = "1. Add\n2. View\n\n0. Exit"
    assert menu_choice_display(options) == expected


def test_single_option_menu():
    # options = ["Exit"]
    # Expected:
    # 0. Exit
    options = ["Exit"]
    expected = "\n0. Exit"
    assert menu_choice_display(options) == expected


def test_two_options_menu():
    # options = ["Continue", "Back"]
    # Expected:
    # 1. Continue
    #
    # 0. Back
    options = ["Continue", "Back"]
    expected = "1. Continue\n\n0. Back"
    assert menu_choice_display(options) == expected
