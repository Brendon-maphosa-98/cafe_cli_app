from src.utils.menu_utils.menu_choice_selection import (
    numbered_display,
    choice_validator,
    list_selection_choice,
)

# Tests for numbered_display function

# happy path


def test_default_numbering_multiple_options():
    # arrange
    menu_name = "products"
    options = ["cheese", "bread", "guacamole"]
    expected_output = "1. Cheese\n2. Bread\n3. Guacamole"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_reserve_zero_for_last_true():
    # arrange
    options = ["add", "view", "exit"]
    expected_output = "1. Add\n2. View\n\n0. Exit"

    # act
    result = numbered_display(options, reserve_zero_for_last=True)

    # assert
    assert result == expected_output


def test_custom_start_index():
    # arrange
    menu_name = "products"
    options = ["apple", "banana", "cherry"]
    expected_output = "3. Apple\n4. Banana\n5. Cherry"

    # act
    result = numbered_display(options, menu_name, start_index=3)

    # assert
    assert result == expected_output


def test_empty_options_returns_custom_empty_message():
    # arrange
    options = []
    expected_output = "No options to display."

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_single_option_with_reserve_zero_for_last():
    # arrange
    options = ["exit"]
    expected_output = "0. Exit"

    # act
    result = numbered_display(options, reserve_zero_for_last=True)
    # assert
    assert result == expected_output


def test_single_option_default_start():
    # arrange
    options = ["cheese"]
    expected_output = "1. Cheese"

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_items_are_displayed_as_given():
    # arrange
    options = ["  apple  ", "BANANA", "ChErRy"]
    expected_output = "1. Apple\n2. Banana\n3. Cherry"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


# edge cases


def test_empty_options_with_custom_menu_name():
    # arrange
    menu_name = "products"
    options = []
    expected_output = f"No {menu_name} to display."

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_contain_only_whitespace_strings():
    # arrange
    options = ["   ", "     "]
    expected_output = "No products to display."
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_with_leading_and_trailing_whitespace():
    # arrange
    options = ["  apple  ", "  banana", "cherry  "]
    expected_output = "1. Apple\n2. Banana\n3. Cherry"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_with_mixed_case_strings_title_applied():
    # arrange
    options = ["aPpLe", "BaNaNa", "CHERRY"]
    expected_output = "1. Apple\n2. Banana\n3. Cherry"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_reserve_zero_for_last_with_single_item():
    # arrange
    options = ["exit"]
    expected_output = "0. Exit"

    # act
    result = numbered_display(options, reserve_zero_for_last=True)

    # assert
    assert result == expected_output


def test_custom_start_index_applied_correctly():
    # arrange
    options = ["apple", "banana", "cherry"]
    expected_output = "5. Apple\n6. Banana\n7. Cherry"

    # act
    result = numbered_display(options, start_index=5)

    # assert
    assert result == expected_output


def test_large_list_numbering_scales_correctly():
    # arrange
    options = [f"item{i}" for i in range(1, 21)]  # 20 items
    expected_output_lines = [f"{i}. Item{i}" for i in range(1, 21)]
    expected_output = "\n".join(expected_output_lines)

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_non_string_option_values_handled():
    # arrange
    options = ["apple", 123, None, "banana"]
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "object has no attribute 'strip'" in result


def test_reserve_zero_for_last_with_whitespace_and_mixed_values():
    # arrange
    options = ["  apple  ", "BANANA", "", "   ", None, "ChErRy"]
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name, reserve_zero_for_last=True)

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "object has no attribute 'strip'" in result


# unhappy path


def test_options_is_not_a_list_returns_error_message():
    # arrange
    menu_name = "products"
    options = "not a list"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "Options must be a list." in result


def test_start_index_is_float_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    # act
    result = numbered_display(options, menu_name, start_index=1.5)  # type: ignore

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "Start index must be an integer." in result


def test_start_index_is_string_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    # act
    result = numbered_display(options, menu_name, start_index="one")  # type: ignore

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "Start index must be an integer." in result


def test_reserve_zero_for_last_not_boolean_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    # act
    result = numbered_display(options, menu_name, reserve_zero_for_last="yes")  # type: ignore

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "reserve_zero_for_last must be a boolean." in result


def test_all_options_are_empty_strings_returns_no_items_message():
    # arrange
    menu_name = "products"
    options = ["", "   ", "     "]
    expected_output = f"No {menu_name} to display."

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_option_contains_non_string_value_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", 123, "banana"]
    expected_output = "An error occurred while generating the list: 'int' object has no attribute 'strip'"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result.startswith("An error occurred while generating the list:")
    assert "object has no attribute 'strip'" in result


# Tests for choice validator function

# happy path


def test_valid_first_option():
    # arrange
    user_input = "1"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == True


def test_valid_middle_option():
    # arrange
    user_input = "2"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == True


def test_valid_last_option():
    # arrange
    user_input = "3"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == True


def test_valid_zero_when_allowed():
    # arrange
    user_input = "0"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check, allow_zero=True)

    # assert
    assert result == True


# edge cases


def test_zero_not_allowed():
    # arrange
    user_input = "0"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check, allow_zero=False)

    # assert
    assert result == "NOT_A_VALID_OPTION"


def test_empty_options_list_with_input_one():
    # arrange
    user_input = "1"
    list_to_check = []

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_VALID_OPTION"


def test_input_equal_to_length_plus_one():
    # arrange
    list_to_check = ["apple", "banana", "cherry"]
    user_input = str(len(list_to_check) + 1)  # "4"

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_VALID_OPTION"


def test_negative_number_input():
    # arrange
    user_input = "-1"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_VALID_OPTION"


# unhappy path


def test_non_numeric_input_letter():
    # arrange
    user_input = "a"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_NUMBER"


def test_non_numeric_input_symbol():
    # arrange
    user_input = "@"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_NUMBER"


def test_non_numeric_input_float_string():
    # arrange
    user_input = "2.5"
    list_to_check = ["apple", "banana", "cherry"]

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result == "NOT_A_NUMBER"


# integration test for list_selection_choice function

import builtins


def test_list_selection_choice_retries_until_valid(monkeypatch, capsys):
    # arrange
    options = ["apple", "banana", "cherry"]
    prompt_message = "Select a fruit"

    # Fake user inputs: first invalid ("x"), then out of range ("5"), then valid ("2")
    fake_inputs = iter(["x", "5", "2"])

    def fake_input(prompt):
        return next(fake_inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    # act
    result = list_selection_choice(options, prompt_message)

    # assert
    assert result == "2"  # the valid input returned

    # Capture printed output
    captured = capsys.readouterr().out
    assert "NOT_A_NUMBER" in captured  # came from first invalid input
    assert "NOT_A_VALID_OPTION" in captured  # came from second invalid input
    assert "1. Apple" in captured  # menu display was printed
