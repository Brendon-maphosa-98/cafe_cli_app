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

def test_input_iterator_runs_out_raises_stopiteration():
    # arrange

    
    # act

    
    # assert
    pass


def test_input_function_raises_keyboardinterrupt():
    # arrange

    
    # act

    
    # assert
    pass


def test_output_function_raises_exception():
    # arrange

    
    # act

    
    # assert
    pass


def test_invalid_menu_name_type_raises_typeerror():
    # arrange

    
    # act

    
    # assert
    pass


def test_infinite_loop_on_continuous_invalid_choices():
    # arrange

    
    # act

    
    # assert
    pass


def test_user_enters_only_special_characters():
    # arrange

    
    # act

    
    # assert
    pass