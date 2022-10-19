"""
    methodes basics
"""
###########
# methodes
###########

# parameters in methodes


# removed uneccecary import


def method_with_parameter_and_return(
    x,
):  # Put x as a parameter in method, pass x as string
    return x
    """
    I passed x as a parameter, the test expected 4 strings as output?
    """
    return

    """this method has a parameter and it will return this paramter value"""
    pass  # what does this do?


def method_with_parameter(
    n,
) -> int:  # Similar solution to method_with_parameter_and_return, however, to test if any parameter value is valid, I passed parameter n, as set datatype as int
    """
    I assigned n as a int, when I put n = 0, it was still the datatype literal, I can imagine running into problems in future tests if I do not assign the proper data-
    values that the tests are expecting. n = int(0) and return n + 1 should give the output 1
    """
    n = int(0)
    return n + 1
    pass


# basic types
def method_with_int_som_return_type() -> int:  # I struggled a bit with this one, and made the test more complicated for myself, until I eventually stumbled upon the seemingly logical solution that was passing -> int to the function rather than as a parameter
    """
    Testing the solution mentioned in the comment above, I returned the value 1, and the test passed as expected.
    """
    return 1
    pass


def method_with_string_som_return_type() -> str:  # as I realised with the method w/ data type int, the solution would be the same with types str and float.
    """
    same solution applied as with method w/ type int.
    """
    return str("string")
    pass


def method_with_float_som_return_type() -> float:  #
    """here I wanted to see if my thought process was correct, so I returned a value of float(1), the method did not return 1.0 and therefore the test failed as it was not specified"""
    return float(1.0)
    pass


def method_with_bool_som_return_type() -> bool:  # solved by calling the bool class and then assigning the bool value to False to return expected output.
    """Test failed when assigned boolean value True, this was expected."""
    return bool(False)
    pass


# Lists
def method_with_string_list() -> list:  # I tried a few different solutions to the list problem, however, calling the class seemed to be best solution.
    """returned list([string1, string2]) as expected, however, I tried also passing list(str([])) to see that it returned the correct data, but that failed"""
    return ["string1", "string2"]
    pass


def method_with_number_list() -> list:  # Similar solution to the previous problem.
    """I also first tried to specify the type to return list(int[]) but this also failed."""
    return [1, 2, 3]
    pass


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


def test_method_with_number_list():
    return_value = method_with_number_list()
    assert type(return_value) == list
    assert return_value == [1, 2, 3]
