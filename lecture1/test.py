"""methodes basics"""
############################
# Your code goes below
############################


def method_with_parameter(x):
    """Method with any parameter"""
    raise NotImplementedError


def method_with_parameter_and_return(x):
    """Method with any parameter and return"""
    raise NotImplementedError


def method_with_int_som_return_type() -> int:
    """Method to return int type"""
    raise NotImplementedError


def method_with_string_som_return_type() -> str:
    """Method to retun str type"""
    raise NotImplementedError


def method_with_float_som_return_type() -> float:
    """Method to return float type"""
    raise NotImplementedError


def method_with_bool_som_return_type() -> bool:
    """Method to return bool type"""
    raise NotImplementedError


# Lists
def method_with_string_list() -> list[str]:
    """Method to return list of strings"""
    raise NotImplementedError


def method_with_string_list_and_parm(x) -> list[str]:
    """Method with input list to return list of strings"""
    raise NotImplementedError


def method_with_number_list() -> list[int]:
    """Method to return list of numbers"""
    raise NotImplementedError


###############################################
# Tests - do not edit anything below this line
###############################################


def test_method_with_parameter():
    assert method_with_parameter("method_with_parameter")
    assert method_with_parameter(1)
    assert method_with_parameter(1.0)
    assert method_with_parameter(True)


def test_method_with_parameter_and_return():
    assert (
        method_with_parameter_and_return("method_with_parameter")
        == "method_with_parameter"
    )
    assert (
        method_with_parameter_and_return(1)
        == 1
    )
    assert (
        method_with_parameter_and_return(1.0)
        == 1.0
    )
    assert method_with_parameter_and_return(True) is True


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
