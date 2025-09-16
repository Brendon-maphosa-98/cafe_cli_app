from src.utils.menu_utils.menu_choice_selection import (
    menu_choices_display,
    menu_selector,
)

### test_menu_choices_display function

# Happy paths


def test_three_options_menu():
    # options = ["Add", "View", "Exit"]
    # Expected:
    # 1. Add
    # 2. View
    #
    # 0. Exit
    options = ["Add", "View", "Exit"]
    expected = "1. Add\n2. View\n\n0. Exit"
    assert menu_choices_display(options) == expected


def test_single_option_menu():
    # options = ["Exit"]
    # Expected:
    # 0. Exit
    options = ["Exit"]
    expected = "\n0. Exit"
    assert menu_choices_display(options) == expected


def test_two_options_menu():
    # options = ["Continue", "Back"]
    # Expected:
    # 1. Continue
    #
    # 0. Back
    options = ["Continue", "Back"]
    expected = "1. Continue\n\n0. Back"
    assert menu_choices_display(options) == expected


### test menu_selector function

## Happy paths


def test_valid_option_in_range(
    monkeypatch,
):  # Simulate validator returning True for input "1"
    monkeypatch.setattr("src.utils.menu_utils.user_input_validation", lambda u, o: True)
    result = menu_selector(["A", "B", "C"], "1")
    assert result == '1'


def test_valid_zero_option(
    monkeypatch,
):  # "0" should also be valid, validator returns True
    monkeypatch.setattr("src.utils.menu_utils.user_input_validation", lambda u, o: True)
    result = menu_selector(["A", "B", "C"], "0")
    assert result == '0'

## Unhappy paths

def test_out_of_range_input(monkeypatch):
    # Validator signals out-of-range input
    monkeypatch.setattr("src.utils.menu_utils.user_input_validation", lambda u, o: "NOT_A_VALID_OPTION")
    result = menu_selector(["A", "B", "C"], "5")
    assert result == "Please select a valid option between 0 and 2"


def test_non_numeric_input_letter(monkeypatch):
    # Validator signals non-numeric input
    monkeypatch.setattr("src.utils.menu_utils.user_input_validation", lambda u, o: "NOT_A_NUMBER")
    result = menu_selector(["A", "B", "C"], "w")
    assert result == "You must select number"


def test_non_numeric_input_symbol(monkeypatch):
    monkeypatch.setattr("src.utils.menu_utils.user_input_validation", lambda u, o: "NOT_A_NUMBER")
    result = menu_selector(["A", "B", "C"], "/")
    assert result == "You must select number"
