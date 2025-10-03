import pytest, sys
from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_list,
    update_existing_item_in_list,
    delete_item_from_list,
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


# ------ update_existing_item_in_list ------

# utility to get the function's defining module for monkeypatching helpers
def _func_module():
    return sys.modules[update_existing_item_in_list.__module__]


# ------------------------------
# Happy path
# ------------------------------

def test_updates_middle_item_success(monkeypatch):
    # Arrange
    m = _func_module()
    products = ["Tea", "Latte", "Mocha"]
    menu_name = "Products"
    outputs = []

    def fake_output(msg):  # capture messages
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        # select index 1 ("Latte")
        assert options is products
        assert menu_name_arg == menu_name
        return 1  # as per docstring: returns int

    def fake_user_prompt_for_new_item(menu_name_arg):
        assert menu_name_arg == menu_name
        return "Flat White"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(products, menu_name, output_fn=fake_output)

    # Assert
    assert result is True
    assert products == ["Tea", "Flat White", "Mocha"]
    # selection message first:
    assert outputs[0] == "You have selected to update: Latte"
    # success message uses menu_name[:-1] ("Products" -> "Product")
    assert outputs[1] == "Product updated successfully to Flat White."


def test_updates_first_item_success_index_zero(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Espresso", "Americano"]
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return 0
    def fake_user_prompt_for_new_item(menu_name_arg): return "Ristretto"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is True
    assert items == ["Ristretto", "Americano"]
    assert outputs[0] == "You have selected to update: Espresso"
    assert outputs[1] == "Product updated successfully to Ristretto."


def test_updates_last_item_success(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Espresso", "Americano", "Cortado"]
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return len(items) - 1
    def fake_user_prompt_for_new_item(menu_name_arg): return "Macchiato"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is True
    assert items == ["Espresso", "Americano", "Macchiato"]
    assert outputs[0] == "You have selected to update: Cortado"
    assert outputs[1] == "Product updated successfully to Macchiato."


def test_allows_duplicate_values_on_update(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Tea", "Latte"]
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return 1  # "Latte"
    def fake_user_prompt_for_new_item(menu_name_arg): return "Tea"  # duplicate allowed

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is True
    assert items == ["Tea", "Tea"]
    assert outputs[0] == "You have selected to update: Latte"
    assert outputs[1] == "Product updated successfully to Tea."


# ------------------------------
# Edge cases
# ------------------------------

def test_empty_list_returns_false_and_message(monkeypatch):
    # Arrange
    m = _func_module()
    items = []
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)

    # (No helper calls expected; early return)
    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is False
    assert outputs == ["The Products list is empty. Returning to Products menu."]


def test_user_cancels_after_selection_returns_none_no_mutation(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Tea", "Latte"]
    original = items.copy()
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return 0  # "Tea"
    def fake_user_prompt_for_new_item(menu_name_arg): return None  # cancellation

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is None
    assert items == original  # no mutation
    # Only the selection message should be emitted; no success message
    assert outputs == ["You have selected to update: Tea"]


def test_empty_menu_name_formats_messages(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Tea"]
    menu_name = ""  # edge: empty menu name
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return 0
    def fake_user_prompt_for_new_item(menu_name_arg): return "Green Tea"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)

    # Assert
    assert result is True
    assert items == ["Green Tea"]
    assert outputs[0] == "You have selected to update: Tea"
    # menu_name[:-1] when menu_name == "" gives "", so expect a leading space then "updated..."
    assert outputs[1] == " updated successfully to Green Tea."


def test_none_list_treated_as_empty_returns_false(monkeypatch):
    # Arrange
    # Although the docstring says a mutable sequence is expected, the implementation
    # treats falsy `list_to_modify` as empty and returns False early.
    m = _func_module()
    items = None
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)

    # Act
    result = update_existing_item_in_list(items, menu_name, output_fn=fake_output)  # type: ignore[arg-type]

    # Assert
    assert result is False
    assert outputs == ["The Products list is empty. Returning to Products menu."]


# ------------------------------
# Unhappy paths (type/contract violations)
# ------------------------------

def test_immutable_sequence_raises_typeerror_on_assignment(monkeypatch):
    # Arrange
    # Violates the "mutable sequence" assumption; tuple cannot be assigned to.
    m = _func_module()
    items = ("Tea", "Latte")  # tuple is immutable
    menu_name = "Products"
    outputs = []

    def fake_output(msg): outputs.append(msg)
    def fake_list_selection_choice(options, prompt, menu_name_arg): return 0
    def fake_user_prompt_for_new_item(menu_name_arg): return "Green Tea"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act & Assert
    with pytest.raises(TypeError):
        update_existing_item_in_list(items, menu_name, output_fn=fake_output)  # type: ignore[arg-type]

    # The selection message is emitted before the failure occurs
    assert outputs == ["You have selected to update: Tea"]


def test_output_fn_must_be_callable(monkeypatch):
    # Arrange
    m = _func_module()
    items = ["Tea"]
    menu_name = "Products"

    def fake_list_selection_choice(options, prompt, menu_name_arg): return 0
    def fake_user_prompt_for_new_item(menu_name_arg): return "Herbal Tea"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act & Assert
    with pytest.raises(TypeError):
        # Passing a non-callable as output_fn should break when the function tries to call it
        update_existing_item_in_list(items, menu_name, output_fn="not a function")  # type: ignore[arg-type]


# TO DO - add tests for delete_item_from_list