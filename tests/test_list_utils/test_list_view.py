from src.utils.list_utils.list_view import list_view


class TestListView:
    """
    Comprehensive test suite for the list_view function.
    Tests cover edge cases, normal operations, and various data types.
    """
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
