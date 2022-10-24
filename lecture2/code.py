#######################################################
"""Personal Tests Below This rectanle! """
#######################################################
"""
def concatinate_strings(string1, string2):
    string1 = "Hello"
    string2 = "World"
    string_concat = ""
    if string_concat != "HelloWorld":
        return string1 + string2
    else:
        return string1, string2 and string_concat            

2nd attempt at using the not in check in Python

def concatinate_strings(string1, string2):
    string1 = "Hello"
    string2 = "World"
    string_concat = ""
    if "HelloWorld" not in string_concat:
        string_concat = string1 + string2
        return string_concat
    if "Hello" not in string2:
        return string1
    if "World" not in string1:
        return string2          
    else:
        return ""

"""
#######################################################
# Regular test cases below this rectangle.
#######################################################
def concatinate_strings(string1, string2):
    string_concat = string1 + string2
    #"%s%s".format(string1, string2)
    #f"{string1}{string2}"
    # #string1 + string2
    return string_concat
# read up on string.join() & f.string & string formatting.


def prefix_string(string, prefix):
    # example of string prefix 
    # new_string = r"Hello, World" - outputs raw string literal.
    # new_string_as_byte = b"Hello, World" - outputs bytes string literal.
    return prefix + string


def suffix_string(string, suffix):
    """
        example if string ends with a specified suffix: "Hello World"; 
        World = suffix, then return True
        else: return False
    """
    return string + suffix


def starts_with(string, prefix):
    """
        test prefix: Hello World -> Starts with He -> return True
        if test prefix Hello World !-> He -> return False
        if Hello = Hello -> return True
        if Hello World = Hello -> return False

    """
    if string.startswith(prefix):
        return True
    else:
        return False    


def ends_with(string, suffix):
    """
        using str.endswith() to test if string "Hello World" ends with "World:
            if "Hello World".endswith("World"):
                return True
            else:
                return False    
    """
    if string.endswith(suffix):
        return True
    else:
        return False    


def get_first_character(string):
    """
        return the index of a given string: "Hello World" expected output: str[0] = H
    """
    return string[0]

def get_last_character(string):
    """
        if we return string[0] we get the first index of a string, however, if we return -1 we recieve the whole index of the string minus one.
    """
    return string[-1]


def get_first_n_characters(string, n):
    return string[0:n] # returns n index of string


def get_last_n_characters(string, n):
    return string[-n:]


def get_substring(string, start, end):
    """
        similar solutions to test at line:100 and test at line:104, we use string slicing to get a start of a substring at: string[substring_start, substring_end]
    """
    return string[start:end]

def welcome(name: str | None, location: str | None) -> str:
    if location == None:
        location = "the world"
    if name == None:
        name = "Unknown"    
    return f"Welcome {name} to {location}"
    
    
    
"""    
    if location != None:
        return "Welcome {name} to {location}".format(name=name, location=location)
    if location == None:
        return "Welcome {name} to the world".format(name=name, location=location)
    if name == None:
        return "Welcome to {location}".format(name=name,location=location)    

    - bad example, does not work!

"""        
