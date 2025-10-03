import pytest
from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_list,
)


"""
Comprehensive test suite for the menu_modification functions.
Tests cover edge cases, normal operations, and various data types.
"""

# ------ user_prompt_for_new_item ------

# happy path


def test_user_enters_valid_item_immediately():
    # arrange
    menu_name = "Products"

    inputs = iter(["latte"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert result == "Latte", "Expected 'Latte' when user enters 'latte'"


def test_user_enters_item_with_whitespace():
    # arrange
    menu_name = "Products"
    inputs = iter(["   bread   "])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert result == "Bread", "Expected 'Bread' when user enters '   bread   '"


def test_user_retries_after_blank_input_and_enters_valid_item():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "1", "croissant"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert result == "Croissant", "Expected 'Croissant' after retrying with valid input"


def test_user_retries_after_invalid_choice_and_enters_valid_item():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "3", "1", "muffin"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert result == "Muffin", "Expected 'Muffin' after retrying with valid input"


def test_user_cancels_after_blank_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "2"])

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )
    # assert
    assert result is None, "Expected None when user cancels operation"
    assert (
        outputs[-1] == f"Operation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


# edge cases


def test_user_repeatedly_enters_blank_then_cancels():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "1", "", "1", "", "2"])

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act

    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when user cancels operation"
    assert (
        outputs[-1] == f"Operation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


def test_user_repeatedly_enters_blank_then_valid_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "1", "", "1", "  ", "1", "espresso"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert (
        result == "Espresso"
    ), "Expected 'Espresso' after multiple retries with valid input"


def test_user_enters_invalid_choices_then_valid_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "3", "0", "yes", "1", "tea"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)

    # assert
    assert (
        result == "Tea"
    ), "Expected 'Tea' after invalid choices followed by valid input"


def test_user_enters_only_spaces_then_valid_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["     ", "1", "sandwich"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert (
        result == "Sandwich"
    ), "Expected 'Sandwich' after entering only spaces followed by valid input"


def test_user_enters_mixed_case_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["cHeEsE cAkE"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)

    # assert
    assert (
        result == "Cheese Cake"
    ), "Expected 'Cheese Cake' when user enters 'cHeEsE cAkE'"


def test_user_enters_whitespace_and_mixed_case_input():
    # arrange
    menu_name = "Products"
    inputs = iter(["   gReEn tEa   "])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)

    # assert
    assert (
        result == "Green Tea"
    ), "Expected 'Green Tea' when user enters '   gReEn tEa   '"


def test_user_prompt_with_single_character_menu_name():
    # arrange
    menu_name = "C"
    inputs = iter(["steve"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)

    # assert
    assert result == "Steve", "Expected 'Steve' when user enters 'steve'"


def test_user_prompt_with_empty_menu_name():
    # arrange
    menu_name = ""
    inputs = iter(["item1"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)
    # assert
    assert result == "Item1", "Expected 'Item1' when user enters 'item1'"


def test_user_cancels_and_outputs_correct_message():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "2"])

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when user cancels operation"
    assert (
        outputs[-1] == f"Operation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


# unhappy path


def test_input_iterator_runs_out_returns_none():
    # arrange
    menu_name = "Products"
    inputs = iter([])  # No inputs provided

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when input iterator runs out"
    assert (
        outputs[-1] == f"\nNo more input available. Returning to {menu_name} menu."
    ), "Expected no more input message"


def test_input_function_raises_keyboardinterrupt_returns_none():
    # arrange
    menu_name = "Products"

    def fake_input(prompt):
        raise KeyboardInterrupt()

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when input function raises KeyboardInterrupt"
    assert (
        outputs[-1] == f"\nOperation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


def test_invalid_menu_name_type_returns_none_with_error_message():
    # arrange
    menu_name = 123  # Invalid type
    inputs = iter(["item1"])

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when menu_name is of invalid type"
    assert (
        outputs[-1]
        == f"\nAn unexpected error occurred: 'int' object is not subscriptable. Returning to {menu_name} menu."
    ), "Expected unexpected error message"


def test_infinite_loop_on_continuous_invalid_choices_eventually_handled():
    # arrange
    menu_name = "Products"
    inputs = iter(["", "3", "0", "yes", "maybe", "1", "tea"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_new_item(menu_name, input_fn=fake_input)

    # assert
    assert (
        result == "Tea"
    ), "Expected 'Tea' after multiple invalid choices followed by valid input"


def test_unexpected_exception_is_caught_and_returns_none():
    # arrange
    menu_name = "Products"

    def fake_input(prompt):
        raise ValueError("Unexpected error")

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_new_item(
        menu_name, input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when unexpected exception is raised"
    assert (
        outputs[-1]
        == f"\nAn unexpected error occurred: Unexpected error. Returning to {menu_name} menu."
    ), "Expected unexpected error message"


# ------ add_new_item_to_list ------

# happy path


def test_adds_unique_item_to_empty_list():
    # arrange
    menu_name = "Products"
    new_item = "Latte"
    lst = []
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, new_item, lst, output_fn=fake_output)

    # assert
    assert result is True
    assert lst == ["Latte"]
    assert outputs[-1] == "Latte added successfully to Products list."


def test_adds_unique_item_to_nonempty_list():
    # arrange
    menu_name = "Products"
    new_item = "Latte"
    lst = ["Tea"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, new_item, lst, output_fn=fake_output)

    # assert
    assert result is True
    assert lst == ["Tea", "Latte"]
    assert outputs[-1] == "Latte added successfully to Products list."


# edge cases


def test_does_not_add_duplicate_item():
    # arrange
    menu_name = "Products"
    new_item = "Latte"
    lst = ["Latte", "Tea"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, new_item, lst, output_fn=fake_output)

    # assert
    assert result is False
    assert lst == ["Latte", "Tea"]
    assert outputs[-1] == "Latte already exists in Products list."


def test_case_sensitivity_treats_different_cases_as_unique():
    # arrange
    menu_name = "Products"
    lst = ["Latte"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, "latte", lst, output_fn=fake_output)

    # assert
    assert result is True
    assert lst == ["Latte", "latte"]
    assert outputs[-1] == "latte added successfully to Products list."


def test_empty_string_as_item_is_added():
    # arrange
    menu_name = "Products"
    lst = []
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, "", lst, output_fn=fake_output)

    # assert
    assert result is True
    assert lst == [""]
    assert outputs[-1] == " added successfully to Products list."


def test_whitespace_string_is_added():
    # arrange
    menu_name = "Products"
    lst = []
    whitespace_item = "   "
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(
        menu_name, whitespace_item, lst, output_fn=fake_output
    )

    # assert
    assert result is True
    assert lst == ["   "]
    assert outputs[-1] == f"{whitespace_item} added successfully to Products list."


def test_works_with_empty_menu_name():
    # arrange
    menu_name = ""
    new_item = "Latte"
    lst = []
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = add_new_item_to_list(menu_name, new_item, lst, output_fn=fake_output)

    # assert
    assert result is True
    assert lst == ["Latte"]
    assert outputs[-1] == "Latte added successfully to  list."


# unhappy path


def test_list_to_modify_is_none_raises_typeerror():
    # arrange
    menu_name = "Products"
    new_item = "Latte"

    # act & assert
    with pytest.raises(TypeError):
        add_new_item_to_list(menu_name, new_item, None)


def test_list_to_modify_is_not_mutable_raises_attributeerror():
    # arrange
    menu_name = "Products"
    new_item = "Latte"
    lst = ("Tea",)  # tuple is immutable

    # act & assert
    with pytest.raises(AttributeError):
        add_new_item_to_list(menu_name, new_item, lst)
