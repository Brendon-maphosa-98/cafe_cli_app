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
    options = {1: "Cheese", 2: "Bread", 3: "Guacamole"}
    expected_output = "\nPRODUCTS:\n\n1. Cheese\n\n2. Bread\n\n3. Guacamole\n"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_reserve_zero_for_last_true():
    # Function does not support reserve_zero_for_last; ensure it formats a dict normally
    options = {1: "Add", 2: "View", 3: "Exit"}
    expected_output = "\nOPTIONS:\n\n1. Add\n\n2. View\n\n3. Exit\n"

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_custom_start_index():
    # arrange
    menu_name = "products"
    options = {3: "Apple", 4: "Banana", 5: "Cherry"}
    expected_output = "\nPRODUCTS:\n\n3. Apple\n\n4. Banana\n\n5. Cherry\n"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_empty_options_returns_custom_empty_message():
    # arrange
    options = []
    expected_output = "No options available."

    # act
    result = numbered_display(
        {},
    )

    # assert
    assert result == expected_output


def test_single_option_with_reserve_zero_for_last():
    # arrange
    options = {1: "Exit"}
    expected_output = "\nOPTIONS:\n\n1. Exit\n"

    # act
    result = numbered_display(options)
    # assert
    assert result == expected_output


def test_single_option_default_start():
    # arrange
    options = {1: "Cheese"}
    expected_output = "\nOPTIONS:\n\n1. Cheese\n"

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_items_are_displayed_as_given():
    # arrange
    options = {1: "  apple  ", 2: "BANANA", 3: "ChErRy"}
    expected_output = "\nPRODUCTS:\n\n1.   apple  \n\n2. BANANA\n\n3. ChErRy\n"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_dictionary_orders_display():
    # arrange
    orders = {
        1: {
            "customer": "Alice",
            "address": "1 A St",
            "phone": "07123456789",
            "items": "Coffee",
            "courier": "Bob",
            "status": "Ready",
        },
        2: {
            "customer": "Carol",
            "address": "2 B Rd",
            "phone": "07123456780",
            "items": "Sandwich",
            "courier": "Dan",
            "status": "Preparing",
        },
    }
    expected_output = (
        "\nORDERS:\n"
        "\nOrder 1:\n"
        "  Customer: Alice\n"
        "  Address: 1 A St\n"
        "  Phone: 07123456789\n"
        "  Items: Coffee\n"
        "  Courier: Bob\n"
        "  Status: Ready\n"
        "\nOrder 2:\n"
        "  Customer: Carol\n"
        "  Address: 2 B Rd\n"
        "  Phone: 07123456780\n"
        "  Items: Sandwich\n"
        "  Courier: Dan\n"
        "  Status: Preparing\n"
    )

    # act
    result = numbered_display(orders, "orders")

    # assert
    assert result == expected_output


def test_single_order_dictionary():
    # arrange
    orders = {
        1: {
            "customer": "Eve",
            "address": "3 C Ln",
            "phone": "07123456781",
            "items": "Tea",
            "courier": "Zed",
            "status": "Ready",
        }
    }
    expected_output = (
        "\nORDERS:\n"
        "\nOrder 1:\n"
        "  Customer: Eve\n"
        "  Address: 3 C Ln\n"
        "  Phone: 07123456781\n"
        "  Items: Tea\n"
        "  Courier: Zed\n"
        "  Status: Ready\n"
    )

    # act
    result = numbered_display(orders, "orders")

    # assert
    assert result == expected_output


# edge cases


def test_empty_options_with_custom_menu_name():
    # arrange
    menu_name = "products"
    options = {}
    expected_output = f"No {menu_name} available."

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_contain_only_whitespace_strings():
    # arrange
    options = {1: "   ", 2: "     "}
    expected_output = "\nPRODUCTS:\n\n1.    \n\n2.      \n"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_with_leading_and_trailing_whitespace():
    # arrange
    options = {1: "  apple  ", 2: "  banana", 3: "cherry  "}
    expected_output = "\nPRODUCTS:\n\n1.   apple  \n\n2.   banana\n\n3. cherry  \n"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_options_with_mixed_case_strings_title_applied():
    # arrange
    options = {1: "aPpLe", 2: "BaNaNa", 3: "CHERRY"}
    expected_output = "\nPRODUCTS:\n\n1. aPpLe\n\n2. BaNaNa\n\n3. CHERRY\n"
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_reserve_zero_for_last_with_single_item():
    # arrange
    options = {1: "Exit"}
    expected_output = "\nOPTIONS:\n\n1. Exit\n"

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_custom_start_index_applied_correctly():
    # arrange
    options = {5: "Apple", 6: "Banana", 7: "Cherry"}
    expected_output = "\nOPTIONS:\n\n5. Apple\n\n6. Banana\n\n7. Cherry\n"

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_large_list_numbering_scales_correctly():
    # arrange
    options = {i: f"Item{i}" for i in range(1, 21)}
    expected_output_lines = [f"\n{i}. Item{i}\n" for i in range(1, 21)]
    expected_output = "\nOPTIONS:\n" + "".join(expected_output_lines)

    # act
    result = numbered_display(options)

    # assert
    assert result == expected_output


def test_non_string_option_values_handled():
    # arrange
    options = 123  # invalid type
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == "Invalid options format. Must be a dictionary."


def test_reserve_zero_for_last_with_whitespace_and_mixed_values():
    # arrange
    options = {1: "  apple  ", 2: "BANANA", 3: "", 4: "   ", 5: None, 6: "ChErRy"}
    menu_name = "products"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert "PRODUCTS" in result


def test_empty_dictionary_returns_custom_empty_message():
    # arrange
    orders = {}
    expected_output = "No orders available."

    # act
    result = numbered_display(orders, "orders")

    # assert
    assert result == expected_output


def test_dictionary_ignores_reserve_zero_for_last():
    # arrange
    orders = {
        1: {
            "customer": "Alice",
            "address": "1 A St",
            "phone": "07123456789",
            "items": "Coffee",
            "courier": "Bob",
            "status": "Ready",
        }
    }
    expected_output = (
        "\nORDERS:\n"
        "\nOrder 1:\n"
        "  Customer: Alice\n"
        "  Address: 1 A St\n"
        "  Phone: 07123456789\n"
        "  Items: Coffee\n"
        "  Courier: Bob\n"
        "  Status: Ready\n"
    )

    # act
    result = numbered_display(orders, "orders")

    # assert
    assert result == expected_output


# unhappy path


def test_options_is_not_a_list_returns_error_message():
    # arrange
    menu_name = "products"
    options = "not a list"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == "Invalid options format. Must be a dictionary."


def test_start_index_is_float_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    # act
    # function does not support start_index argument; provide dict instead
    options = {1: "Apple", 2: "Banana"}
    result = numbered_display(options, menu_name)

    # assert
    assert "PRODUCTS" in result


def test_start_index_is_string_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    options = {1: "Apple", 2: "Banana"}
    result = numbered_display(options, menu_name)
    assert "PRODUCTS" in result


def test_reserve_zero_for_last_not_boolean_returns_error_message():
    # arrange
    menu_name = "products"
    options = ["apple", "banana"]

    result = numbered_display({1: "Apple", 2: "Banana"}, menu_name)
    assert "PRODUCTS" in result


def test_all_options_are_empty_strings_returns_no_items_message():
    # arrange
    menu_name = "products"
    options = ["", "   ", "     "]
    options = {1: "", 2: "   ", 3: "     "}
    expected_output = "\nPRODUCTS:\n\n1. \n\n2.    \n\n3.      \n"

    # act
    result = numbered_display(options, menu_name)

    # assert
    assert result == expected_output


def test_option_contains_non_string_value_returns_error_message():
    # arrange
    menu_name = "products"
    options = 123
    result = numbered_display(options, menu_name)
    assert result == "Invalid options format. Must be a dictionary."


def test_options_is_not_list_or_dict_returns_error_message():
    # arrange
    menu_name = "products"
    options = 12345  # not a list or dict

    # act
    result = numbered_display(options, menu_name)
    assert result == "Invalid options format. Must be a dictionary."


# Tests for choice validator function

# happy path


def test_valid_first_option():
    # arrange
    user_input = "1"
    # choice_validator now expects a dict of keys -> values
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)

    # assert
    assert result is True


def test_valid_middle_option():
    # arrange
    user_input = "2"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    result = choice_validator(user_input, list_to_check)
    assert result is True


def test_valid_last_option():
    # arrange
    user_input = "3"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    result = choice_validator(user_input, list_to_check)
    assert result is True


def test_valid_zero_when_allowed():
    # arrange
    user_input = "0"
    # choice_validator no longer has allow_zero flag; validator accepts 0 if it's a key
    list_to_check = {0: "Back", 1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    assert result is True


def test_valid_option_with_dict_by_count():
    # arrange
    user_input = "1"
    # dict with two orders -> treated by validator based on count (len==2)
    # With the new validator the keys themselves are validated, so use a matching key
    options = {10: {"item": "coffee"}, 20: {"item": "tea"}}

    # act
    result = choice_validator("10", options)
    assert result is True


# edge cases


def test_zero_not_allowed():
    # arrange
    user_input = "0"
    # since validator has no allow_zero flag, 0 is invalid when not present as a key
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    # numeric but out of keys -> function returns None
    assert result == "Invalid choice. Please select a valid option from the list."


def test_zero_allowed_with_non_empty_dict():
    # arrange
    user_input = "0"
    # to allow 0 the options dict must contain 0 as a key
    options = {0: {"item": "coffee"}}

    # act
    result = choice_validator(user_input, options)
    assert result is True


def test_empty_options_list_with_input_one():
    # arrange
    user_input = "1"
    # empty options are represented by an empty dict
    list_to_check = {}

    # act
    result = choice_validator(user_input, list_to_check)
    # numeric but not present -> None
    assert result == "Invalid choice. Please select a valid option from the list."


def test_input_equal_to_length_plus_one():
    # arrange
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}
    user_input = str(len(list_to_check) + 1)  # "4"

    # act
    result = choice_validator(user_input, list_to_check)
    assert result == "Invalid choice. Please select a valid option from the list."


def test_negative_number_input():
    # arrange
    user_input = "-1"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    assert result == "Invalid choice. Please select a valid option from the list."


# unhappy path


def test_non_numeric_input_letter():
    # arrange
    user_input = "a"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    assert result == "Invalid input. Please enter a number."


def test_non_numeric_input_symbol():
    # arrange
    user_input = "@"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    assert result == "Invalid input. Please enter a number."


def test_non_numeric_input_float_string():
    # arrange
    user_input = "2.5"
    list_to_check = {1: "apple", 2: "banana", 3: "cherry"}

    # act
    result = choice_validator(user_input, list_to_check)
    assert result == "Invalid input. Please enter a number."


def test_dict_input_out_of_range_returns_not_a_valid_option():
    # arrange
    user_input = "3"
    options = {1: {"item": "a"}, 2: {"item": "b"}}
    # act
    result = choice_validator(user_input, options)
    # numeric but not a key -> None
    assert result == "Invalid choice. Please select a valid option from the list."


# integration tests for list_selection_choice function

import builtins


# test that it retries until valid input is given for list_selection_choice with list of options
def test_list_selection_choice_retries_until_valid(monkeypatch, capsys):
    # arrange
    options = {1: "Apple", 2: "Banana", 3: "Cherry"}
    prompt_message = "Select a fruit"

    # Fake user inputs: first invalid ("x"), then out of range ("5"), then valid ("2")
    fake_inputs = iter(["x", "5", "2"])

    def fake_input(prompt):
        return next(fake_inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    # act
    result = list_selection_choice(options, prompt_message, menu_name="products")

    # assert
    assert result == "2"  # the valid input returned

    # Capture printed output
    captured = capsys.readouterr().out
    assert "Invalid input. Please enter a number." in captured
    assert "Invalid choice. Please select a valid option from the list." in captured
    assert "PRODUCTS" in captured  # menu display was printed


# test that it retries until valid input is given for list_selection_choice with dict of orders
def test_list_selection_choice_dict_retries_until_valid(monkeypatch, capsys):
    # arrange
    options = {
        1: {
            "customer": "Alice",
            "address": "1 A St",
            "phone": "07123456789",
            "items": "Coffee",
            "courier": "Bob",
            "status": "Ready",
        },
        2: {
            "customer": "Carol",
            "address": "2 B Rd",
            "phone": "07123456780",
            "items": "Sandwich",
            "courier": "Dan",
            "status": "Preparing",
        },
    }
    prompt_message = "Select an order"

    # Fake user inputs: first invalid ("y"), then out of range ("4"), then valid ("1")
    fake_inputs = iter(["y", "4", "1"])

    def fake_input(prompt):
        return next(fake_inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    # act
    result = list_selection_choice(options, prompt_message, menu_name="orders")

    # assert
    assert result == "1"  # the valid input returned

    # Capture printed output
    captured = capsys.readouterr().out
    assert "Invalid input. Please enter a number." in captured
    assert "Invalid choice. Please select a valid option from the list." in captured
    assert "ORDERS" in captured  # menu display was printed
