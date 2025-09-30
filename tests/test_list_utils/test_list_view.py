from src.utils.list_utils.list_choice_selection import list_view
import pytest

"""
comprehensive test suite for the list_view function.
tests cover edge cases, normal operations, and various data types.
"""

class TestListView:
    menu = "items"

    def test_empty_list_returns_message(self):
        assert list_view([], self.menu) == "No items to display."


    def test_single_item_numbered_correctly(self):
        assert list_view(["Coffee"], self.menu) == "1. Coffee"


    def test_multiple_items_are_numbered_and_separated_by_newlines(self):
        items = ["Espresso", "Latte", "Tea"]
        result = list_view(items, self.menu)
        # exact match ensures numbering, order, and separation are correct
        assert result == "1. Espresso\n2. Latte\n3. Tea"
        # sanity check: newline count should be len(items) - 1
        assert result.count("\n") == len(items) - 1


    def test_unicode_and_special_characters_preserved(self):
        items = ["Crème brûlée", "Emoji ☕️"]
        expected = "1. Crème brûlée\n2. Emoji ☕️"
        assert list_view(items, self.menu) == expected


    def test_internal_newlines_in_items_preserved_and_no_trailing_newline(self):
        items = ["Line\nBreak", "End"]
        result = list_view(items, self.menu)
        # verify internal newline survived
        assert "Line\nBreak" in result
        # verify last line is exactly last numbered item (no trailing newline)
        assert result.endswith("2. End")


    def test_does_not_mutate_input_list(self):
        items = ["A", "B"]
        before = items.copy()
        _ = list_view(items, self.menu)
        assert items == before

    # edge cases

    def test_items_none_returns_no_message(self):
    # None is falsy -> early-return path
        assert list_view(None, "Couriers") == "No Couriers to display."

    def test_empty_menu_name_with_empty_items_shows_blank_menu_in_message(self):
        # Current behaviour: fallback for empty menu_name only runs when items is truthy,
        # so an empty list + empty menu_name yields "No  to display." (likely a bug).
        assert list_view([], "") == "No  to display."

    def test_empty_menu_name_with_nonempty_items_uses_items_fallback(self):
        # When items present, empty menu_name is replaced with "items"
        assert list_view(["A"], "") == "1. A"

    def test_items_containing_only_empty_strings_returns_empty_string(self):
        # All items skipped -> display_str remains empty -> returns empty string
        assert list_view(["", ""], "Things") == ""

    def test_skips_empty_strings_and_numbers_dont_increment(self):
        # enumerate advances index even for skipped (empty) items -> numbering gap
        assert list_view(["A", "", "B"], "Things") == "1. A\n2. B"

    def test_menu_name_none_triggers_type_error_message(self):
        # len(menu_name) will raise TypeError and function returns the TypeError message
        assert list_view(["A"], None) == "Invalid input: items or menu name must be a list of strings."

    def test_items_as_string_iterates_characters(self):
        # Passing a string (not a list) will iterate characters -> numbered chars
        assert list_view("AB", "Letters") == "1. A\n2. B"

    def test_non_string_items_are_stringified_in_output(self):
        # Non-string items are converted to their string representation
        assert list_view([1, None, True], "Vals") == "1. 1\n2. None\n3. True"

    def test_large_list_no_trailing_newline(self):
        items = [f"item{i}" for i in range(1, 1001)]
        result = list_view(items, "Items")
        assert result.endswith("1000. item1000")
        # ensure no trailing newline
        assert not result.endswith("\n")

    # unhappy paths

    def test_menu_name_none_returns_type_error_message(self):
        assert list_view(["A"], None) == "Invalid input: items or menu name must be a list of strings."

    def test_items_not_iterable_returns_type_error_message(self):
    # int is not iterable -> enumerate will raise TypeError which the function catches
        assert list_view(123, "Items") == "Invalid input: items or menu name must be a list of strings."

    def test_menu_name_not_string_returns_type_error_message(self):
    # len(menu_name) will raise TypeError for non-sized non-string types like int
        assert list_view(["A"], 123) == "Invalid input: items or menu name must be a list of strings."

    def test_call_without_menu_name_raises_typeerror_at_call_site(self):
    # Missing required positional argument -> Python raises TypeError before entering function
        with pytest.raises(TypeError):
            list_view(["A"])  # type: ignore # missing menu_name
