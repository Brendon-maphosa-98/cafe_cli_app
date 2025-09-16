# test_menu_choice_validator.py

from utils.menu_utils.user_input_validation import menu_choice_validator


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


def test_valid_input_last_option():  # input "3", choices ["a", "b", "c"] - should return True (last menu choice)
    user_input = "3"
    choices = ["a", "b", "c"]
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


### Edge cases


def test_empty_choices_with_zero():  # input "0", choices [] - should return True (back is always valid even if no choices)
    user_input = "0"
    choices = []
    expected = True
    assert expected == menu_choice_validator(user_input, choices)


def test_empty_choices_with_nonzero():  # input "1", choices [] - should return False (no menu options available)
    user_input = "1"
    choices = []
    expected = False
    assert expected == menu_choice_validator(user_input, choices)


def test_negative_input():  # input "-1", choices ["a", "b"] - should return False
    user_input = "-1"
    choices = ["a", "b"]
    expected = False
    assert expected == menu_choice_validator(user_input, choices)


def test_input_equal_to_len_choices_plus_one():  # input "4", choices ["a", "b", "c"] (len=3) - should return False (out of range)
    user_input = "4"
    choices = ["a", "b", "c"]
    expected = False
    assert expected == menu_choice_validator(user_input, choices)


### Unhappy path


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
