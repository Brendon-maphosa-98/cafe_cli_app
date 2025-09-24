from src.utils.list_utils.list_view import list_view


class TestListView:
    """
    Comprehensive test suite for the list_view function.
    Tests cover edge cases, normal operations, and various data types.
    """

    # Test empty inputs
    def test_empty_list(self):
        """Test function with empty list."""
        result = list_view([])
        assert result == "No items to display."

    def test_none_input(self):
        """Test function with None input."""
        result = list_view(None)
        assert result == "No items to display."

    # Test single item
    def test_single_string_item(self):
        """Test function with single string item."""
        items = ["Apple"]
        result = list_view(items)
        expected = "1. Apple"
        assert result == expected

    def test_single_number_item(self):
        """Test function with single numeric item."""
        items = [42]
        result = list_view(items)
        expected = "1. 42"
        assert result == expected

    def test_single_boolean_item(self):
        """Test function with single boolean item."""
        items = [True]
        result = list_view(items)
        expected = "1. True"
        assert result == expected

    # Test multiple items
    def test_multiple_string_items(self):
        """Test function with multiple string items."""
        items = ["Coffee", "Tea", "Hot Chocolate"]
        result = list_view(items)
        expected = "1. Coffee\n2. Tea\n3. Hot Chocolate"
        assert result == expected

    def test_multiple_number_items(self):
        """Test function with multiple numeric items."""
        items = [1, 2, 3, 4, 5]
        result = list_view(items)
        expected = "1. 1\n2. 2\n3. 3\n4. 4\n5. 5"
        assert result == expected

    def test_mixed_data_types(self):
        """Test function with mixed data types."""
        items = ["Apple", 42, True, 3.14, None]
        result = list_view(items)
        expected = "1. Apple\n2. 42\n3. True\n4. 3.14\n5. None"
        assert result == expected

    # Test special string cases
    def test_empty_strings(self):
        """Test function with empty strings as items."""
        items = ["", "Item", ""]
        result = list_view(items)
        expected = "1. \n2. Item\n3. "
        assert result == expected

    def test_strings_with_spaces(self):
        """Test function with strings containing spaces."""
        items = ["Item One", "Item Two", "Item Three"]
        result = list_view(items)
        expected = "1. Item One\n2. Item Two\n3. Item Three"
        assert result == expected

    def test_strings_with_special_characters(self):
        """Test function with strings containing special characters."""
        items = ["Item@#$", "Item%^&", "Item*()"]
        result = list_view(items)
        expected = "1. Item@#$\n2. Item%^&\n3. Item*()"
        assert result == expected

    def test_strings_with_newlines(self):
        """Test function with strings containing newlines."""
        items = ["Item\nOne", "Item Two", "Item\nThree\nFour"]
        result = list_view(items)
        expected = "1. Item\nOne\n2. Item Two\n3. Item\nThree\nFour"
        assert result == expected

    # Test large lists
    def test_ten_items(self):
        """Test function with ten items."""
        items = [f"Item {i}" for i in range(1, 11)]
        result = list_view(items)
        expected = "\n".join([f"{i}. Item {i}" for i in range(1, 11)])
        assert result == expected

    def test_large_list(self):
        """Test function with large list (100 items)."""
        items = [f"Item {i}" for i in range(1, 101)]
        result = list_view(items)
        lines = result.split("\n")
        assert len(lines) == 100
        assert lines[0] == "1. Item 1"
        assert lines[99] == "100. Item 100"

    # Test edge cases with numbering
    def test_numbering_starts_at_one(self):
        """Verify numbering starts at 1, not 0."""
        items = ["First", "Second", "Third"]
        result = list_view(items)
        assert result.startswith("1. First")
        assert "2. Second" in result
        assert "3. Third" in result

    def test_no_trailing_newline(self):
        """Verify result doesn't end with trailing newline."""
        items = ["Item1", "Item2"]
        result = list_view(items)
        assert not result.endswith("\n\n")
        assert result.endswith("2")  # Should end with the last item content

    # Test different iterable types
    def test_tuple_input(self):
        """Test function with tuple input."""
        items = ("Apple", "Banana", "Cherry")
        result = list_view(items)
        expected = "1. Apple\n2. Banana\n3. Cherry"
        assert result == expected

    def test_set_input(self):
        """Test function with set input (order may vary)."""
        items = {"Apple", "Banana", "Cherry"}
        result = list_view(items)
        lines = result.split("\n")
        assert len(lines) == 3
        assert all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines))
        # Check all items are present (order doesn't matter for sets)
        result_items = [line.split(". ", 1)[1] for line in lines]
        assert set(result_items) == {"Apple", "Banana", "Cherry"}

    def test_generator_input(self):
        """Test function with generator input."""

        def item_generator():
            yield "Item A"
            yield "Item B"
            yield "Item C"

        result = list_view(item_generator())
        expected = "1. Item A\n2. Item B\n3. Item C"
        assert result == expected

    # Test complex objects
    def test_objects_with_str_method(self):
        """Test function with objects that have __str__ method."""

        class CustomObject:
            def __init__(self, name):
                self.name = name

            def __str__(self):
                return f"CustomObject({self.name})"

        items = [CustomObject("A"), CustomObject("B")]
        result = list_view(items)
        expected = "1. CustomObject(A)\n2. CustomObject(B)"
        assert result == expected

    # Performance and stress tests
    def test_very_long_string_items(self):
        """Test function with very long string items."""
        long_string = "A" * 1000
        items = [long_string, "Short", long_string]
        result = list_view(items)
        lines = result.split("\n")
        assert len(lines) == 3
        assert lines[0] == f"1. {long_string}"
        assert lines[1] == "2. Short"
        assert lines[2] == f"3. {long_string}"

    # Test falsy values
    def test_falsy_values(self):
        """Test function with various falsy values."""
        items = [0, False, "", None]
        result = list_view(items)
        expected = "1. 0\n2. False\n3. \n4. None"
        assert result == expected

    def test_whitespace_only_strings(self):
        """Test function with whitespace-only strings."""
        items = [" ", "  ", "\t", "\n"]
        result = list_view(items)
        expected = "1.  \n2.   \n3. \t\n4. \n"
        assert result == expected
