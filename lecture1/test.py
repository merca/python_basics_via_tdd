"""
    methodes basics
"""
###########
# methodes
###########

# parameters in methodes


# removed uneccecary import


import re


def method_with_parameter_and_return(x):
    """Returns x

    Args:
        x (str): Input string

    Returns:
        str: Returns the input string
    """
    return x


def method_with_parameter(
    n,
) -> int:
    """Just a method with a parameter

    Args:
        n (Any): Any parameter and its not used

    Returns:
        int: just returns 1
    """
    return int(0 + 1)


# basic types
def method_with_int_som_return_type() -> int:
    """Method to retun int type

    Returns:
        int: returns type int
    """
    return 1


def method_with_string_som_return_type() -> str:
    """Method to retun str type"""
    return str("string")


def method_with_float_som_return_type() -> float:  #
    """
    here I wanted to see if my thought process was correct, so I returned a value of float(1),
    the method did not return 1.0 and therefore the test failed as it was not specified
    """
    return float(1.0)


def method_with_bool_som_return_type() -> bool:  # solved by calling the bool class and then assigning the bool value to False to return expected output.
    """Test failed when assigned boolean value True, this was expected."""
    return bool(False)


# Lists
def method_with_string_list() -> list[
    str
]:  # I tried a few different solutions to the list problem, however, calling the class seemed to be best solution.
    """returned list([string1, string2]) as expected, however, I tried also passing list(str([])) to see that it returned the correct data, but that failed"""
    return ["string1", "string2"]


def method_with_string_list_and_parm(stringlist: list) -> list[str]:
    return stringlist


def method_with_number_list() -> list[int]:  # Similar solution to the previous problem.
    """I also first tried to specify the type to return list(int[]) but this also failed."""
    return [1, 2, 3]


###############################################
# My tests since lack variation
###############################################


###############################################
# Tests - do not edit anything below this line
###############################################


def test_method_with_parameter():
    assert method_with_parameter("method_with_parameter")


def test_method_with_parameter_and_return():
    assert (
        method_with_parameter_and_return("method_with_parameter")
        == "method_with_parameter"
    )
    assert (
        method_with_parameter_and_return("another_string_as_input")
        == "another_string_as_input"
    )
    assert (
        method_with_parameter_and_return("yet_another_string_as_input")
        == "yet_another_string_as_input"
    )
    assert method_with_parameter_and_return("one_more") == "one_more"


def test_method_with_int_som_return_type():
    return_value = method_with_int_som_return_type()
    assert type(return_value) == int
    assert return_value == 1


def test_method_with_string_som_return_type():
    return_value = method_with_string_som_return_type()
    assert type(return_value) == str
    assert return_value == "string"


def test_method_with_float_som_return_type():
    return_value = method_with_float_som_return_type()
    assert type(return_value) == float
    assert return_value == 1.0


def test_method_with_bool_som_return_type():
    return_value = method_with_bool_som_return_type()
    assert type(return_value) == bool
    assert return_value is False


def test_method_with_string_list():
    return_value = method_with_string_list()
    assert type(return_value) == list
    assert return_value == ["string1", "string2"]


def test_method_with_list_paramter():
    return_value = method_with_string_list_and_parm(["string1", "string2"])
    assert type(return_value) == list
    assert return_value == ["string1", "string2"]
    return_value = method_with_string_list_and_parm([])
    assert type(return_value) == list


def test_method_with_number_list():
    return_value = method_with_number_list()
    assert type(return_value) == list
    assert return_value == [1, 2, 3]
