# test_menu_choice_validator.py


def test_valid_input_first_index():  # input "0", choices ["a", "b"] → should return True
    pass


def test_valid_input_last_index():  # input "1", choices ["a", "b"] → should return True
    pass


### Edge cases


def test_empty_choices_with_zero():  # input "0", choices [] → should return False or invalid signal
    pass


def test_negative_input():  # input "-1", choices ["a", "b"] → should return False
    pass


def test_input_equal_to_last_index():  # input "len(choices)-1", e.g. "2" with choices ["x","y","z"] → should return True
    pass


### Unhappy path


def test_input_too_large_for_choices():  # input "2", choices ["a", "b"] → should return False
    pass


def test_input_far_too_large():  # input "100", choices ["a","b"] → should return False
    pass


def test_non_numeric_letter():  # input "w", choices ["a","b"] → should return ValueError or "NOT_A_NUMBER"
    pass


def test_non_numeric_symbol():  # input "/", choices ["a","b"] → should return ValueError or "NOT_A_NUMBER"
    pass


def test_float_string_input():  # input "2.5", choices ["a","b"] → should return ValueError or "NOT_A_NUMBER"
    pass


def test_empty_string_input():  # input "", choices ["a","b"] → should return ValueError or "NOT_A_NUMBER"
    pass


def test_none_as_input():  # input None, choices ["a","b"] → should return ValueError or "NOT_A_NUMBER"
    pass


def test_choices_not_iterable():  # input "0", choices=None → should error or return False
    pass
