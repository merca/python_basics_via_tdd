import pytest

from .code import (add_number_to_every_element_in_array,
                   add_one_to_every_element_in_array,
                   check_if_element_in_array_can_be_divided_by_number,
                   find_elements_that_contains_letter, reverce_string,
                   summarize_all_elements_in_array,
                   summarize_elements_in_array_start_and_end_index)


def test_summarize_all_elements_in_array():
    assert summarize_all_elements_in_array([1, 2, 3]) == 6
    assert summarize_all_elements_in_array([1, 2, 3, 4, 5]) == 15
    assert summarize_all_elements_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert summarize_all_elements_in_array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55


def test_summarize_all_elements_in_array_with_negative_numbers():
    assert summarize_all_elements_in_array([-1, -2, -3]) == -6
    assert summarize_all_elements_in_array([-1, -2, -3, -4, -5]) == -15
    assert summarize_all_elements_in_array(
        [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == -45
    assert summarize_all_elements_in_array(
        [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -55


def test_summarize_elements_in_array_start_and_end_index():
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 0, 2) == 6
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 0, 4) == 15
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 0, 5) == 15
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 2, 4) == 9
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 2, 5) == 9
    assert summarize_elements_in_array_start_and_end_index(
        [1, 2, 3, 4, 5], 4, 5) == 5


def test_summarize_elements_in_array_start_and_end_index_with_negative_numbers():
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 0, 2) == -6
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 0, 4) == -15
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 0, 5) == -15
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 2, 4) == -9
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 2, 5) == -9
    assert summarize_elements_in_array_start_and_end_index(
        [-1, -2, -3, -4, -5], 4, 5) == -5


def test_summarize_elements_in_array_start_and_end_index_with_invalid_index():
    with pytest.raises(IndexError):
        summarize_elements_in_array_start_and_end_index(
            [1, 2, 3, 4, 5], 0, 6)
    with pytest.raises(IndexError):
        summarize_elements_in_array_start_and_end_index(
            [1, 2, 3, 4, 5], 6, 7)
    with pytest.raises(IndexError):
        summarize_elements_in_array_start_and_end_index(
            [1, 2, 3, 4, 5], 6, 5)


def test_add_one_to_every_element_in_array():
    assert add_one_to_every_element_in_array([1, 2, 3]) == [2, 3, 4]
    assert add_one_to_every_element_in_array(
        [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert add_one_to_every_element_in_array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert add_one_to_every_element_in_array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_add_number_to_every_element_in_array():
    assert add_number_to_every_element_in_array([1, 2, 3], 2) == [3, 4, 5]
    assert add_number_to_every_element_in_array(
        [1, 2, 3, 4, 5], 11) == [12, 13, 14, 15, 16]
    assert add_number_to_every_element_in_array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], -5) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]


def test_check_if_element_in_array_can_be_divided_by_number():
    assert check_if_element_in_array_can_be_divided_by_number(
        [1, 2, 3], 2) == [False, True, False]
    assert check_if_element_in_array_can_be_divided_by_number(
        [1, 2, 3, 4, 5], 3) == [False, False, True, False, False]
    assert check_if_element_in_array_can_be_divided_by_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [False, True, False, True, False, True, False, True, False]


def test_find_elements_that_contains_letter():
    assert find_elements_that_contains_letter(
        ["Merca", "Agne", "Jørgen"], "e") == ["Merca", "Agne", "Jørgen"]
    assert find_elements_that_contains_letter(
        ["Merca", "Agne", "Jørgen"], "a") == ["Merca", "Agne"]
    assert find_elements_that_contains_letter(
        ["Merca", "Agne", "Jørgen"], "ø") == ["Jørgen"]


def test_reverce_string():
    assert reverce_string("Merca") == "acreM"
    assert reverce_string("Agne") == "engA"
    assert reverce_string("Jørgen") == "negrøJ"
