"""
Comprehensive test suite for menu choice selection utilities.

This module contains tests for the menu choice selection functions:
- `menu_choice_validator`: Validates raw user input against available menu options
- `menu_choices_display`: Formats menu options for display with proper numbering
- `menu_selection_validator`: Provides user-facing validation messages

Tests include happy paths, edge cases, invalid inputs, display formatting,
and validator-integration tests using `monkeypatch` for controlled behavior.
"""

from src.utils.menu_utils.menu_choice_selection import (
    menu_choices_display,
    menu_selection_validator,
    menu_choice_validator,
)


class TestMenuChoiceSelection:
    """
    All test cases for menu choice selection utilities.
    """

    # ===== menu_choice_validator Tests =====

    def test_valid_input_zero(self):
        user_input = "0"
        choices = ["a", "b", "c"]
        assert True == menu_choice_validator(user_input, choices)

    def test_valid_input_first_option(self):
        user_input = "1"
        choices = ["a", "b", "c"]
        assert True == menu_choice_validator(user_input, choices)

    def test_valid_input_middle_option(self):
        user_input = "2"
        choices = ["a", "b", "c"]
        assert True == menu_choice_validator(user_input, choices)

    def test_valid_input_last_option(self):
        user_input = "2"
        choices = ["a", "b", "c"]
        assert True == menu_choice_validator(user_input, choices)

    # Edge cases
    def test_empty_choices_with_zero(self):
        user_input = "0"
        choices = []
        assert True == menu_choice_validator(user_input, choices)

    def test_empty_choices_with_nonzero(self):
        user_input = "1"
        choices = []
        assert "NOT_A_VALID_OPTION" == menu_choice_validator(user_input, choices)

    def test_negative_input(self):
        user_input = "-1"
        choices = ["a", "b"]
        assert "NOT_A_VALID_OPTION" == menu_choice_validator(user_input, choices)

    def test_input_equal_to_len_choices_plus_one(self):
        user_input = "4"
        choices = ["a", "b", "c"]
        assert "NOT_A_VALID_OPTION" == menu_choice_validator(user_input, choices)

    # Invalid input types
    def test_non_numeric_letter(self):
        user_input = "w"
        choices = ["a", "b", "c"]
        assert "NOT_A_NUMBER" == menu_choice_validator(user_input, choices)

    def test_non_numeric_symbol(self):
        user_input = "/"
        choices = ["a", "b", "c"]
        assert "NOT_A_NUMBER" == menu_choice_validator(user_input, choices)

    def test_float_string_input(self):
        user_input = "2.5"
        choices = ["a", "b", "c"]
        assert "NOT_A_NUMBER" == menu_choice_validator(user_input, choices)

    def test_empty_string_input(self):
        user_input = ""
        choices = ["a", "b", "c"]
        assert "NOT_A_NUMBER" == menu_choice_validator(user_input, choices)

    # ===== menu_choices_display Tests =====

    def test_three_options_menu(self):
        options = ["Add", "View", "Exit"]
        expected = "1. Add\n2. View\n\n0. Exit"
        assert menu_choices_display(options) == expected

    def test_single_option_menu(self):
        options = ["Exit"]
        expected = "\n0. Exit"
        assert menu_choices_display(options) == expected

    def test_two_options_menu(self):
        options = ["Continue", "Back"]
        expected = "1. Continue\n\n0. Back"
        assert menu_choices_display(options) == expected

    # ===== menu_selection_validator Tests =====

    def test_valid_option_in_range(self, monkeypatch):
        # Mock the menu_choice_validator to return True for valid input
        monkeypatch.setattr(
            "src.utils.menu_utils.menu_choice_selection.menu_choice_validator",
            lambda u, o: True,
        )
        result = menu_selection_validator(["A", "B", "C"], "1")
        assert result == "1"

    def test_valid_zero_option(self, monkeypatch):
        monkeypatch.setattr(
            "src.utils.menu_utils.menu_choice_selection.menu_choice_validator",
            lambda u, o: True,
        )
        result = menu_selection_validator(["A", "B", "C"], "0")
        assert result == "0"

    def test_out_of_range_input(self, monkeypatch):
        monkeypatch.setattr(
            "src.utils.menu_utils.menu_choice_selection.menu_choice_validator",
            lambda u, o: "NOT_A_VALID_OPTION",
        )
        result = menu_selection_validator(["A", "B", "C"], "5")
        assert result == "Please select a valid option between 0 and 2"

    def test_non_numeric_input_letter(self, monkeypatch):
        monkeypatch.setattr(
            "src.utils.menu_utils.menu_choice_selection.menu_choice_validator",
            lambda u, o: "NOT_A_NUMBER",
        )
        result = menu_selection_validator(["A", "B", "C"], "w")
        assert result == "You must select number"

    def test_non_numeric_input_symbol(self, monkeypatch):
        monkeypatch.setattr(
            "src.utils.menu_utils.menu_choice_selection.menu_choice_validator",
            lambda u, o: "NOT_A_NUMBER",
        )
        result = menu_selection_validator(["A", "B", "C"], "/")
        assert result == "You must select number"


# ====== new test cases for refactored functions in menu_modification.py ======

