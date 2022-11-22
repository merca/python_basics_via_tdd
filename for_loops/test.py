import pytest

from .code import (
    add_number_to_every_element_in_array,
    add_one_to_every_element_in_array,
    check_if_element_in_array_can_be_divided_by_number,
    check_if_string_contains_only_digits,
    check_if_string_contains_only_letters,
    find_duplicate_number_in_array,
    find_elements_that_contains_letter,
    find_missing_number_in_array,
    fizz_buzz,
    maximum_wealth,
    return_only_odd_numbers,
    reverce_string,
    running_sum_in_array,
    split_array_into_multiple_parts,
    split_array_into_two_parts,
    summarize_all_elements_in_array,
    summarize_elements_in_array_start_and_end_index,
)


def test_summarize_all_elements_in_array():
    assert summarize_all_elements_in_array([1, 2, 3]) == 6
    assert summarize_all_elements_in_array([1, 2, 3, 4, 5]) == 15
    assert summarize_all_elements_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert summarize_all_elements_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55


def test_summarize_all_elements_in_array_with_negative_numbers():
    assert summarize_all_elements_in_array([-1, -2, -3]) == -6
    assert summarize_all_elements_in_array([-1, -2, -3, -4, -5]) == -15
    assert summarize_all_elements_in_array([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == -45
    assert (
        summarize_all_elements_in_array([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
        == -55
    )


def test_summarize_elements_in_array_start_and_end_index():
    assert summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5], 0, 2) == 6
    assert summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5], 0, 4) == 15
    assert summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5], 0, 5) == 15
    assert summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5], 2, 4) == 12
    assert summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5], 2, 5) == 12
    assert (
        summarize_elements_in_array_start_and_end_index([1, 2, 3, 4, 5, 6], 4, 5) == 11
    )


def test_summarize_elements_in_array_start_and_end_index_with_negative_numbers():
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5], 0, 2)
        == -6
    )
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5], 0, 4)
        == -15
    )
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5], 0, 5)
        == -15
    )
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5], 2, 4)
        == -12
    )
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5], 2, 5)
        == -12
    )
    assert (
        summarize_elements_in_array_start_and_end_index([-1, -2, -3, -4, -5, -6], 4, 5)
        == -11
    )


def test_add_one_to_every_element_in_array():
    assert add_one_to_every_element_in_array([1, 2, 3]) == [2, 3, 4]
    assert add_one_to_every_element_in_array([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert add_one_to_every_element_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
    assert add_one_to_every_element_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
    ]


def test_add_number_to_every_element_in_array():
    assert add_number_to_every_element_in_array([1, 2, 3], 2) == [3, 4, 5]
    assert add_number_to_every_element_in_array([1, 2, 3, 4, 5], 11) == [
        12,
        13,
        14,
        15,
        16,
    ]
    assert add_number_to_every_element_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9], -5) == [
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4,
    ]


def test_check_if_element_in_array_can_be_divided_by_number():
    assert check_if_element_in_array_can_be_divided_by_number([1, 2, 3], 2) == [
        False,
        True,
        False,
    ]
    assert check_if_element_in_array_can_be_divided_by_number([1, 2, 3, 4, 5], 3) == [
        False,
        False,
        True,
        False,
        False,
    ]
    assert check_if_element_in_array_can_be_divided_by_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], 2
    ) == [False, True, False, True, False, True, False, True, False]


def test_find_elements_that_contains_letter():
    assert find_elements_that_contains_letter(["Merca", "Jane", "John"], "e") == [
        "Merca",
        "Jane",
    ]
    assert find_elements_that_contains_letter(["Merca", "Jane", "John"], "a") == [
        "Merca",
        "Jane",
    ]
    assert find_elements_that_contains_letter(["Merca", "Jane", "John"], "n") == [
        "Jane",
        "John",
    ]


def test_reverce_string():
    assert reverce_string("Merca") == "acreM"
    assert reverce_string("Jane") == "enaJ"
    assert reverce_string("John") == "nhoJ"


def test_split_array_into_two_parts():
    assert split_array_into_two_parts([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_array_into_two_parts([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_array_into_two_parts([1, 2, 3, 4, 5, 6, 7]) == [
        [1, 2, 3, 4],
        [5, 6, 7],
    ]
    assert split_array_into_two_parts([1, 2, 3, 4, 5, 6, 7, 8]) == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    assert split_array_into_two_parts([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9],
    ]


def test_split_array_into_multiple_parts():
    assert split_array_into_multiple_parts([1, 2, 3, 4, 5], 3) == [[1, 2], [3, 4], [5]]
    assert split_array_into_multiple_parts([1, 2, 3, 4, 5, 6], 3) == [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
    assert split_array_into_multiple_parts([1, 2, 3, 4, 5, 6, 7], 4) == [
        [1, 2],
        [3, 4],
        [5, 6],
        [7],
    ]
    assert split_array_into_multiple_parts([1, 2, 3, 4, 5, 6, 7, 8], 3) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8],
    ]
    assert split_array_into_multiple_parts([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9],
    ]


def test_return_only_odd_numbers():
    assert return_only_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert return_only_odd_numbers([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert return_only_odd_numbers([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7]
    assert return_only_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 3, 5, 7]
    assert return_only_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]


def test_check_if_string_contains_only_digits():
    assert check_if_string_contains_only_digits("123") is True
    assert check_if_string_contains_only_digits("123a") is False
    assert check_if_string_contains_only_digits("123a456") is False
    assert check_if_string_contains_only_digits("123456") is True


def test_check_if_string_contains_only_letters():
    assert check_if_string_contains_only_letters("abc") is True
    assert check_if_string_contains_only_letters("abc1") is False
    assert check_if_string_contains_only_letters("abc1def") is False
    assert check_if_string_contains_only_letters("abcdef") is True


def test_fizz_buzz():
    assert fizz_buzz(3) == ["1", "2", "Fizz"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_running_sum_in_array():
    assert running_sum_in_array([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum_in_array([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum_in_array([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


def test_find_missing_number_in_array():
    assert find_missing_number_in_array([0, 1, 2, 3, 4, 6, 7, 8, 9]) == 5
    assert find_missing_number_in_array([0, 1, 2, 3, 4, 5, 6, 7, 9]) == 8
    assert find_missing_number_in_array([0, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert find_missing_number_in_array([0, 1, 2, 3, 4, 5, 6, 7, 8]) == None


def test_find_duplicate_number_in_array():
    assert find_duplicate_number_in_array([1, 2, 2, 4, 5, 6, 7, 8, 9]) == 2
    assert find_duplicate_number_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == 9
    assert find_duplicate_number_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == None


def test_maximum_wealth():
    assert maximum_wealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert maximum_wealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
