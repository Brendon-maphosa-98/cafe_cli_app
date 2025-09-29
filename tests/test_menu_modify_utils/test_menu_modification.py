from src.utils.menu_modify_utils.menu_modification import user_prompt_for_new_item
import pytest

"""
Comprehensive test suite for the menu_modification functions.
Tests cover edge cases, normal operations, and various data types.
"""

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
