import pytest, sys
from src.utils.menu_modify_utils.menu_modification import (
    user_prompt_for_new_item,
    add_new_item_to_list,
    update_existing_item_in_list,
    delete_item_from_list,
    user_prompt_for_order_customer_name,
    user_prompt_for_order_customer_address,
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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Ristretto"

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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return len(items) - 1

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Macchiato"

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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 1  # "Latte"

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Tea"  # duplicate allowed

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

    def fake_output(msg):
        outputs.append(msg)

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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0  # "Tea"

    def fake_user_prompt_for_new_item(menu_name_arg):
        return None  # cancellation

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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Green Tea"

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

    def fake_output(msg):
        outputs.append(msg)

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

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Green Tea"

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

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0

    def fake_user_prompt_for_new_item(menu_name_arg):
        return "Herbal Tea"

    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    monkeypatch.setattr(m, "user_prompt_for_new_item", fake_user_prompt_for_new_item)

    # Act & Assert
    with pytest.raises(TypeError):
        # Passing a non-callable as output_fn should break when the function tries to call it
        update_existing_item_in_list(items, menu_name, output_fn="not a function")  # type: ignore[arg-type]


# happy path


def test_delete_item_from_list_deletes_middle_item():
    """Ensures an item in the middle of a non-empty list is correctly deleted and success messages are printed."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 1  # select "Latte"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act

    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()

    # assert
    assert result is True
    assert lst == ["Tea", "Mocha"]
    assert outputs[0] == "You have selected to delete: Latte"
    assert outputs[1] == "Product deleted successfully."


def test_delete_item_from_list_deletes_first_item():
    """Ensures the first item in the list is correctly deleted and appropriate confirmation is shown."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0  # select "Tea"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert lst == ["Latte", "Mocha"]
    assert outputs[0] == "You have selected to delete: Tea"
    assert outputs[1] == "Product deleted successfully."


def test_delete_item_from_list_deletes_last_item():
    """Ensures the last item in the list is correctly deleted and appropriate confirmation is shown."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 2  # select "Mocha"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert lst == ["Tea", "Latte"]
    assert outputs[0] == "You have selected to delete: Mocha"
    assert outputs[1] == "Product deleted successfully."


def test_delete_item_from_list_user_cancels():
    """Verifies that when the user cancels (None returned), no deletion occurs and the list remains unchanged."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    original = lst.copy()
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return None  # simulate user cancellation

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is None
    assert lst == original  # no mutation


# edge cases


def test_delete_item_from_list_with_single_item():
    """Checks deletion works correctly when the list contains only one element, leaving it empty afterwards."""
    # arrange
    menu_name = "Products"
    lst = ["Tea"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0  # select the only item "Tea"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert lst == []
    assert outputs[0] == "You have selected to delete: Tea"
    assert outputs[1] == "Product deleted successfully."


def test_delete_item_from_list_with_empty_list():
    """Confirms function short-circuits gracefully when called with an empty list and returns False."""
    # arrange
    menu_name = "Products"
    lst = []
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    m = _func_module()
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    # assert
    assert result is False
    assert outputs == ["The Products list is empty. Returning to Products menu."]


def test_delete_item_from_list_with_irregular_plural_menu_name():
    """Validates behaviour when menu_name is an irregular plural (e.g. 'People'), ensuring function still operates."""
    # arrange
    menu_name = "Peoples"
    lst = ["Alice", "Bob", "Charlie"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 1  # select "Bob"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert lst == ["Alice", "Charlie"]
    assert outputs[0] == "You have selected to delete: Bob"
    assert outputs[1] == "People deleted successfully."


def test_delete_item_from_list_with_large_list():
    """Ensures function handles deletion correctly in very large lists (e.g. 1000+ items) without performance issues."""
    # arrange
    menu_name = "Items"
    lst = [f"Item{i}" for i in range(1000)]  # large list of 1000 items
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 500  # select "Item500"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert len(lst) == 999
    assert "Item500" not in lst
    assert outputs[0] == "You have selected to delete: Item500"
    assert outputs[1] == "Item deleted successfully."


# unhappy path


def test_delete_item_from_list_out_of_range_index():
    """Checks function raises IndexError if list_selection_choice returns an invalid index beyond list bounds."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 5  # out-of-range index

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act & assert
    with pytest.raises(IndexError):
        delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()


def test_delete_item_from_list_non_integer_index():
    """Verifies ValueError is raised if list_selection_choice returns a non-integer value."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte", "Mocha"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return "one"  # non-integer index

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act & assert
    with pytest.raises(ValueError):
        delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()


def test_delete_item_from_list_with_empty_menu_name():
    """Confirms function still executes but produces malformed messages when menu_name is an empty string."""
    # arrange
    menu_name = ""
    lst = ["Tea", "Latte"]
    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0  # select "Tea"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act
    result = delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    # assert
    assert result is True
    assert lst == ["Latte"]
    assert outputs[0] == "You have selected to delete: Tea"
    # menu_name is "", so expect leading space then "deleted successfully."
    assert outputs[1] == " deleted successfully."


def test_delete_item_from_list_output_fn_raises_exception():
    """Ensures any exception raised by the provided output_fn is propagated and not swallowed."""
    # arrange
    menu_name = "Products"
    lst = ["Tea", "Latte"]

    def fake_output(msg):
        raise RuntimeError("Output function failed")

    def fake_list_selection_choice(options, prompt, menu_name_arg):
        return 0  # select "Tea"

    m = _func_module()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(m, "list_selection_choice", fake_list_selection_choice)
    # act & assert
    with pytest.raises(RuntimeError) as exc_info:
        delete_item_from_list(lst, menu_name, output_fn=fake_output)
    monkeypatch.undo()
    assert str(exc_info.value) == "Output function failed"


# ------ user_prompt_for_order_customer_name (happy path) ------


def test_user_prompt_for_order_customer_name_valid_immediate():
    # arrange
    inputs = iter(["john", "doe"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_name(input_fn=fake_input)

    # assert
    assert result == (
        "John",
        "Doe",
    ), "Expected ('John', 'Doe') for inputs 'john', 'doe'"


def test_user_prompt_for_order_customer_name_whitespace_and_mixed_case():
    # arrange
    inputs = iter(["   aLiCe  ", "  bRoWn"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_name(input_fn=fake_input)

    # assert
    assert result == (
        "Alice",
        "Brown",
    ), "Expected ('Alice', 'Brown') after stripping and titling"


def test_user_prompt_for_order_customer_name_single_letter_names():
    # arrange
    inputs = iter(["a", "b"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_name(input_fn=fake_input)

    # assert
    assert result == ("A", "B"), "Expected ('A', 'B') for single-letter names"


# ------ user_prompt_for_order_customer_name (edge cases) ------


def test_user_cancels_during_empty_name_prompt():
    # arrange
    inputs = iter(["", "", "2"])  # first name blank, last name blank, then cancel

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = user_prompt_for_order_customer_name(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None
    assert outputs[-1] == "Operation cancelled. Returning to Orders menu."


def test_user_provides_hyphen_and_apostrophe_names():
    # arrange - names with hyphen and apostrophe should be accepted
    inputs = iter(["anne-marie", "o'neill"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_name(input_fn=fake_input)

    # assert
    assert result == ("Anne-Marie", "O'Neill")


# ------ user_prompt_for_order_customer_name (unhappy paths) ------


def test_user_provides_invalid_characters_then_cancels():
    # arrange
    inputs = iter(["John3", "Doe", "2"])  # invalid first name then cancel

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = user_prompt_for_order_customer_name(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None
    assert outputs[-1] == "Operation cancelled. Returning to Orders menu."


def test_order_prompt_input_iterator_runs_out_returns_none():
    # arrange
    inputs = iter([])  # no inputs

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = user_prompt_for_order_customer_name(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None
    assert outputs[-1] == "\nNo more input available. Returning to Orders menu."


def test_order_prompt_input_fn_raises_keyboardinterrupt_returns_none():
    # arrange

    def fake_input(prompt):
        raise KeyboardInterrupt()

    outputs = []

    def fake_output(msg):
        outputs.append(msg)

    # act
    result = user_prompt_for_order_customer_name(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None
    assert outputs[-1] == "\nOperation cancelled. Returning to Orders menu."


# ------ user_prompt_customer_address (happy path) ------


def test_user_prompt_for_order_customer_address_valid_input():
    """Checks that the function correctly returns a formatted address when valid street, city, and postcode are entered."""
    # arrange
    inputs = iter(["123 Baker St", "London", "NW1 6XE"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == ("123 Baker St, London, NW1 6XE")


def test_user_prompt_for_order_customer_address_handles_lowercase_input():
    """Ensures that mixed or lowercase input is properly formatted (title/upper-cased) before returning."""
    # arrange
    inputs = iter(["456 elm street", "manchester", "m1 1ae"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == ("456 Elm Street, Manchester, M1 1AE")


def test_user_prompt_for_order_customer_address_valid_with_extra_spaces():
    """Verifies that leading/trailing spaces in user input are stripped and a valid address is still accepted."""
    # arrange
    inputs = iter(["   789 Oak Rd   ", "   Bristol   ", "   BS1 5TR   "])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == ("789 Oak Rd, Bristol, BS1 5TR")


# ------ user_prompt_customer_address (edge cases) ------


def test_user_prompt_for_order_customer_address_minimal_valid_input():
    """Tests the shortest valid input (e.g., '1 A St, B, A1 1AA') to confirm regex boundary conditions."""
    # arrange
    inputs = iter(["1 A St", "B", "A1 1AA"])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == ("1 A St, B, A1 1AA")


def test_user_prompt_for_order_customer_address_max_length_input():
    """Checks that a long but valid address (near reasonable character limits) still passes validation."""
    # arrange
    long_street = "12345 Long Street Name That Exceeds Normal Lengths"
    long_city = "A Very Long City Name Indeed"
    long_postcode = "AB12 3CD"
    inputs = iter([long_street, long_city, long_postcode])

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == (f"{long_street}, {long_city}, {long_postcode}")


def test_user_prompt_for_order_customer_address_retry_after_invalid():
    """Simulates a user entering an invalid address first, then correcting it successfully on retry."""
    # arrange
    # 3 invalid attempts, then retry input then valid inputs
    inputs = iter(
        [
            "NoNumber St",  # invalid street
            "City",  # valid city
            "A1 1AA",  # valid postcode
            "1",  # retry prompt
            "123 Valid St",  # retry street
            "Valid City",  # retry city
            "B2 2BB",  # retry postcode
        ]
    )

    def fake_input(prompt):
        return next(inputs)

    # act
    result = user_prompt_for_order_customer_address(input_fn=fake_input)
    # assert
    assert result == ("123 Valid St, Valid City, B2 2BB")


def test_user_prompt_for_order_customer_address_keyboard_interrupt():
    """Ensures graceful handling when the user triggers a KeyboardInterrupt during input (returns None)."""
    # arrange
    menu_name = "Orders"

    def fake_input(prompt):
        raise KeyboardInterrupt()

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None on KeyboardInterrupt"
    assert (
        outputs[-1] == f"\nOperation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


def test_user_prompt_for_order_customer_address_stop_iteration():
    """Ensures graceful handling of StopIteration when mock input runs out of data (returns None)."""
    # arrange
    menu_name = "Orders"
    inputs = iter([])  # no inputs

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None on StopIteration"
    assert (
        outputs[-1] == f"\nNo more input available. Returning to {menu_name} menu."
    ), "Expected no more input message"


def test_user_prompt_for_order_customer_address_empty_fields_then_cancel():
    """Simulates user leaving fields blank, then choosing to cancel when prompted, expecting a None return."""
    # arrange
    menu_name = "Orders"
    inputs = iter(
        [
            "",  # empty street
            "",  # empty city
            "",  # empty postcode
            "2",  # choose to cancel
        ]
    )

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when user cancels after empty inputs"
    assert (
        outputs[-1] == f"Operation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


# ------ user_prompt_customer_address (unhappy paths) ------


def test_user_prompt_for_order_customer_address_invalid_format_then_cancel():
    """Simulates user entering an incorrectly formatted address, then choosing to cancel when prompted."""
    # arrange
    menu_name = "Orders"
    inputs = iter(
        [
            "NoNumber St",  # invalid street
            "City",  # valid city
            "A1 1AA",  # valid postcode
            "2",  # choose to cancel
        ]
    )

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result is None, "Expected None when user cancels after invalid input"
    assert (
        outputs[-1] == f"Operation cancelled. Returning to {menu_name} menu."
    ), "Expected cancellation message"


def test_user_prompt_for_order_customer_address_invalid_retry_then_valid():
    """Simulates a user entering invalid data, choosing retry, and then successfully entering a valid address."""
    # arrange
    inputs = iter(
        [
            "NoNumber St",  # invalid street
            "City",  # valid city
            "A1 1AA",  # valid postcode
            "1",  # choose to retry
            "123 Valid St",  # retry street
            "Valid City",  # retry city
            "B2 2BB",  # retry postcode
        ]
    )

    def fake_input(prompt):
        return next(inputs)

    outputs = []

    def fake_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=fake_output
    )

    # assert
    assert result == (
        "123 Valid St, Valid City, B2 2BB"
    ), "Expected valid address after retry"


def test_user_prompt_for_order_customer_address_unexpected_exception():
    """Forces an unexpected exception inside the function and confirms it is caught and handled gracefully.

    The test simulates an internal exception (from the input function). The function should catch
    the exception, call `output_fn` with an explanatory message, and return None.
    """
    # arrange
    menu_name = "Orders"

    def fake_input(prompt):
        # Simulate an unexpected runtime error during input
        raise ValueError("Unexpected error")

    outputs = []

    def safe_output(message):
        outputs.append(message)

    # act
    result = user_prompt_for_order_customer_address(
        input_fn=fake_input, output_fn=safe_output
    )

    # assert
    assert result is None
    assert (
        outputs[-1]
        == f"\nAn unexpected error occurred: Unexpected error. Returning to {menu_name} menu."
    )
