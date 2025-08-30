from error_checking_module import user_int_check

import pytest 

### error check module unit tests

## user input check function test

# Common cases

def test_input_is_integer():
    # arrange
    input = 5
    minrng = 1
    maxrng = 8
    expected = True

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_input_is_string_number():
    # arrange
    input = '5'
    minrng = 1
    maxrng = 8
    expected = True

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_minrng_is_larger_than_input():
    # arrange
    input = 5
    minrng = 6
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_maxrng_is_less_than_input():
    # arrange
    input = 5
    minrng = 1
    maxrng = 4
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'
    

# Edge cases 

def test_input_is_float_with_no_precision():
    # arrange
    input = 5.0
    minrng = 1
    maxrng = 8
    expected = True

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_input_is_float_with_precision():
    # arrange
    input = 5.5
    minrng = 1
    maxrng = 8
    expected = True

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'


def test_input_is_string_float_version_of_int():
    # arrange
    input = '5.0'
    minrng = 1
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_input_is_string_float_version_of_float():
    # arrange
    input = "5.5"
    minrng = 1
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'


# Corner case

def test_input_is_string_letter():
    # arrange
    input = 't'
    minrng = 1
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_input_is_string_special_char():
    # arrange
    input = '&'
    minrng = 1
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

def test_input_is_space():
    # arrange
    input = ' '
    minrng = 1
    maxrng = 8
    expected = None

    # act

    result = user_int_check(input,minrng,maxrng)

    # assert

    assert expected == result, f'expected {expected} but got {result}'

