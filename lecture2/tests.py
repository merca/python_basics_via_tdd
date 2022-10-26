from pytest import raises
from .code import *


def test_concatinate_strings():
    assert concatinate_strings("Hello", "World") == "HelloWorld"
    assert concatinate_strings("Hello", "") == "Hello"
    assert concatinate_strings("", "World") == "World"
    assert concatinate_strings("", "") == ""


def test_prefix_string():
    assert prefix_string("Hello", "Hi") == "HiHello"
    assert prefix_string("Hello", "") == "Hello"
    assert prefix_string("", "Hi") == "Hi"
    assert prefix_string("", "") == ""


def test_suffix_string():
    assert suffix_string("Hello", "World") == "HelloWorld"
    assert suffix_string("Hello", "") == "Hello"
    assert suffix_string("", "World") == "World"
    assert suffix_string("", "") == ""


def test_starts_with():
    assert starts_with("Hello", "He") == True
    assert starts_with("Hello", "Hi") == False
    assert starts_with("Hello", "Hello") == True
    assert starts_with("Hello", "World") == False
    assert starts_with("Hello", "") == True


def test_ends_with():
    assert ends_with("Hello", "lo") == True
    assert ends_with("Hello", "World") == False
    assert ends_with("Hello", "Hello") == True
    assert ends_with("Hello", "Hello World") == False
    assert ends_with("Hello", "") == True


def test_create_sentence():
    assert create_sentence(["Hello", "World"]) == "Hello World"
    assert (
        create_sentence(["Hello", "World", "How", "Are", "You"])
        == "Hello World How Are You"
    )
    assert (
        create_sentence(["Hello", "World", "How", "Are", "You"], "_")
        == "Hello_World_How_Are_You"
    )
    assert (
        create_sentence(["Hello", "World", "How", "Are", "You"], "**")
        == "Hello**World**How**Are**You"
    )


def test_get_first_character():
    assert get_first_character("Hello") == "H"
    assert get_first_character("World") == "W"
    with raises(IndexError):
        get_first_character("")


def test_get_last_character():
    assert get_last_character("Hello") == "o"
    assert get_last_character("World") == "d"
    with raises(IndexError):
        get_last_character("")


def test_get_first_n_characters():
    assert get_first_n_characters("Hello", 2) == "He"
    assert get_first_n_characters("Hello", 5) == "Hello"
    assert get_first_n_characters("Hello", 6) == "Hello"
    assert get_first_n_characters("", 2) == ""


def test_get_last_n_characters():
    assert get_last_n_characters("Hello", 2) == "lo"
    assert get_last_n_characters("Hello", 5) == "Hello"
    assert get_last_n_characters("Hello", 6) == "Hello"
    assert get_last_n_characters("", 2) == ""


def test_get_substring():
    assert get_substring("Hello", 0, 2) == "He"
    assert get_substring("Hello", 0, 5) == "Hello"
    assert get_substring("Hello", 0, 6) == "Hello"
    assert get_substring("Hello", 2, 5) == "llo"
    assert get_substring("Hello", 2, 6) == "llo"
    assert get_substring("Hello", 5, 6) == ""
    assert get_substring("Hello", 6, 6) == ""
    assert get_substring("Hello", 0, 0) == ""
    assert get_substring("Hello", 1, 0) == ""
    assert get_substring("Hello", 6, 5) == ""
    assert get_substring("Hello", 6, 0) == ""


def test_concatinate_strings():
    assert concatinate_strings("Hello", "World") == "HelloWorld"
    assert concatinate_strings("Hello", "") == "Hello"
    assert concatinate_strings("", "World") == "World"
    assert concatinate_strings("", "") == ""


def test_welcome():
    assert welcome("John", "London") == "Welcome John to London"
    assert welcome("Jane", "Paris") == "Welcome Jane to Paris"
    assert welcome("Jack", "New York") == "Welcome Jack to New York"
    assert welcome(name="Jill", location=None) == "Welcome Jill to the world"
    assert welcome(name=None, location="London") == "Welcome Unknown to London"
