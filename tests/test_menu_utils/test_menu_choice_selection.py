from src.utils.menu_utils.menu_choice_selection import (
    menu_choices_display,
    menu_selection_validator,
    menu_choice_validator,
)

# test_menu_choice_validator.py

# Happy paths


def test_valid_input_zero():  # input "0", choices ["a", "b", "c"] - should return True
    user_input = "0"
    choices = ["a", "b", "c"]
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


def test_valid_input_first_option():  # input "1", choices ["a", "b", "c"] - should return True
    user_input = "1"
    choices = ["a", "b", "c"]
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


def test_valid_input_middle_option():  # input "2", choices ["a", "b", "c"] - should return True
    user_input = "2"
    choices = ["a", "b", "c"]
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


def test_valid_input_last_option():  # input "2", choices ["a", "b", "c"] - should return True (last menu choice, not 3 as 0 will be an available option)
    user_input = "2"
    choices = ["a", "b", "c"]
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


### Edge cases


def test_empty_choices_with_zero():  # input "0", choices [] - should return True (back is always valid even if no choices)
    user_input = "0"
    choices = []
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


def test_empty_choices_with_nonzero():  # input "1", choices [] - should return "NOT_A_VALID_OPTION" (no menu options available except return)
    user_input = "1"
    choices = []
    expected = "NOT_A_VALID_OPTION"
    assert expected == menu_choice_validator(user_input, choices)


def test_negative_input():  # input "-1", choices ["a", "b"] - should return "NOT_A_VALID_OPTION"
    user_input = "-1"
    choices = ["a", "b"]
    expected = "NOT_A_VALID_OPTION"
    assert expected == menu_choice_validator(user_input, choices)


def test_input_equal_to_len_choices_plus_one():  # input "4", choices ["a", "b", "c"] (len=3) - should return "NOT_A_VALID_OPTION" (out of range)
    user_input = "4"
    choices = ["a", "b", "c"]
    expected = "NOT_A_VALID_OPTION"
    assert expected == menu_choice_validator(user_input, choices)


### Unhappy paths


def test_non_numeric_letter():  # input "w", choices ["a","b","c"] - should return ValueError or NOT_A_NUMBER
    user_input = "w"
    choices = ["a", "b", "c"]
    expected = "NOT_A_NUMBER"
    assert expected == menu_choice_validator(user_input, choices)


def test_non_numeric_symbol():  # input "/", choices ["a","b","c"] - should return ValueError or NOT_A_NUMBER
    user_input = "/"
    choices = ["a", "b", "c"]
    expected = "NOT_A_NUMBER"
    assert expected == menu_choice_validator(user_input, choices)


def test_float_string_input():  # input "2.5", choices ["a","b","c"] - should return ValueError or NOT_A_NUMBER
    user_input = "2.5"
    choices = ["a", "b", "c"]
    expected = "NOT_A_NUMBER"
    assert expected == menu_choice_validator(user_input, choices)


def test_empty_string_input():  # input "", choices ["a","b","c"] - should return ValueError or NOT_A_NUMBER
    user_input = ""
    choices = ["a", "b", "c"]
    expected = "NOT_A_NUMBER"
    assert expected == menu_choice_validator(user_input, choices)


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


### test menu_selection_validator function

## Happy paths


def test_valid_option_in_range(
    monkeypatch,
):  # Simulate validator returning True for input "1"
    monkeypatch.setattr("src.utils.menu_utils.menu_choice_selection", lambda u, o: True)
    result = menu_selection_validator(["A", "B", "C"], "1")
    assert result == "1"


def test_valid_zero_option(
    monkeypatch,
):  # "0" should also be valid, validator returns True
    monkeypatch.setattr("src.utils.menu_utils.menu_choice_selection", lambda u, o: True)
    result = menu_selection_validator(["A", "B", "C"], "0")
    assert result == "0"


## Unhappy paths


def test_out_of_range_input(monkeypatch):
    # Validator signals out-of-range input
    monkeypatch.setattr(
        "src.utils.menu_utils.menu_choice_selection", lambda u, o: "NOT_A_VALID_OPTION"
    )
    result = menu_selection_validator(["A", "B", "C"], "5")
    assert result == "Please select a valid option between 0 and 2"


def test_non_numeric_input_letter(monkeypatch):
    # Validator signals non-numeric input
    monkeypatch.setattr(
        "src.utils.menu_utils.menu_choice_selection", lambda u, o: "NOT_A_NUMBER"
    )
    result = menu_selection_validator(["A", "B", "C"], "w")
    assert result == "You must select number"


def test_non_numeric_input_symbol(monkeypatch):
    monkeypatch.setattr(
        "src.utils.menu_utils.menu_choice_selection", lambda u, o: "NOT_A_NUMBER"
    )
    result = menu_selection_validator(["A", "B", "C"], "/")
    assert result == "You must select number"
