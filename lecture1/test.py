"""
    methodes basics
"""
###########
# methodes
###########

# parameters in methodes
def test_method_with_parameter_and_return():
    """hva denne gjør"""
    pass  # hva denne gjør


def method_with_parameter():
    pass


# basic types
def method_with_int_som_return_type():
    pass


def method_with_string_som_return_type():
    pass


def test_method_with_float_som_return_type():
    pass


def test_method_with_bool_som_return_type():
    pass


# Lists
def test_method_with_string_list():
    pass


def test_method_with_number_list():
    pass


###############################################
# Tests - do not edit anything below this line
###############################################


def test_method_with_parameter():
    assert method_with_parameter("method_with_parameter")


def test_method_with_parameter_and_return():
    assert (
        test_method_with_parameter_and_return("method_with_parameter")
        == "method_with_parameter"
    )


def test_method_with_int_som_return_type():
    return_value = method_with_int_som_return_type()
    assert type(return_value) == int
    assert return_value == 1


def test_method_with_string_som_return_type():
    return_value = method_with_string_som_return_type()
    assert type(return_value) == str
    assert return_value == "string"


def test_method_with_float_som_return_type():
    return_value = test_method_with_float_som_return_type()
    assert type(return_value) == float
    assert return_value == 1.0


def test_method_with_bool_som_return_type():
    return_value = test_method_with_bool_som_return_type()
    assert type(return_value) == bool
    assert return_value == False


def test_method_with_string_list():
    return_value = test_method_with_string_list()
    assert type(return_value) == list
    assert return_value == ["string1", "string2"]


def test_method_with_number_list():
    return_value = test_method_with_number_list()
    assert type(return_value) == list
    assert return_value == [1, 2, 3]
