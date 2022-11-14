from __future__ import annotations

def summarize_all_elements_in_array(array):
    """
    Summarize all elements in array
    Use for loop
    """
    sum_of_elements = 0
    for a in array:
        sum_of_elements = sum_of_elements + a
    return sum_of_elements

"""
    first iteration:
        a = array[0] = 1
        sum_of_elements = sum_of_elements(0) + a(1) = 1
    second iteration:
        a = array[1] = 2
        sum_of_elements = (1) + 2 = 3    
    third iteration:
        a = array[2] = 3
        sum_of_elements = (3) + 3 = 6
    finished iterating:
        return sum_of_elements(6)      
"""

def summarize_elements_in_array_start_and_end_index(array, start_index, end_index):
    """
    Summarize elements in array from start_index to end_index
    Use for loop
    """
    sum_of_elements = 0
    index_at = 0
    for elements in array:
        if index_at < start_index:
            index_at = index_at + 1
            continue
        sum_of_elements = sum_of_elements + elements
        if index_at == end_index:
            break
        index_at = index_at + 1
    return sum_of_elements
"""
in this test, we have assigned two local variables before we start iterating through the loop
these variables are:
sum_of_elements = 0
index_at = 0
    
    first iteration:
        elements = array[0] = 1 
        if index_at < start_index: # index_at = 0, start_index = array[0]
            index_at = index_at + 1 = index_at = 1
            continue # loop continues 
        sum_of_elements = 0 + elements = array[0] = (0 + 1 + 2 + 3) = 6
        if index_at == end_index: # index_at = 1, end_index = array[-1] = 5
            break # breaks the loop when index_at is equal to the last index of the array, in this case, 5.
        index_at = index_at + 1 = 2 
    
    second iteration:
        elements = array[0-1] = 1,2,3,4,5
        sum_of_elements = sum_of_elements + elements(0 + 1 + 2 + 4 + 5) = 15
    
    third iteration:
        elements = array[0-1] = 1,2,3,4,5
        sum_of_elements = sum_of_elements + elements(0 + 1 + 2 + 4 + 5) = 15

    fourth iteration:
        elements = array[0-1] = 1,2,3,4,5 - > checks for index[2,4] = 2 & 5
        sum_of_elements  = sum_of_elements + elements(2 + 2 + 3 + 5) = 12
    fifth iteration:
        elements = array[0-1] = 1,2,3,4,5 - > checks for index[4,5] = 5 & 6 
        sum_of_elements = sum_of_elements + elements(5 + 6) = 11
    finished iterating:
        return [6, 15, 15, 12, 12, 11]      


    






        


"""



def add_one_to_every_element_in_array(array):
    """
    Add one to every element in array
    Use for loop
    """
    new_array = []
    for a in array:
        new_array.append(a + 1)
    return new_array
"""
    first iteration:
        a = array[0] = 1
        [] = 1 + 1 = [2]
    second iteration:
        a = array[1] = 2
        [2] = [2] + 2 + 1 = [2,3]
    third iteration:
        a = array[2] = 3
        [2,3] = 3 + 1 = [2,3,4]
    finished iterating:
        return [2,3,4]             
"""       


def add_number_to_every_element_in_array(array, number):
    """
    Add number to every element in array
    Use for loop
    """
    new_array = []
    for a in array:
        new_array.append(a + number)
    return new_array    
"""
    first iteration:
    number = 2
        a = array[0] = 1
        [] = 1 + 2 = [3]
    second iteration:
        a = array[1] = 2
        [3] = [2] + 2 + 2 = [3,4]
    third iteration:
        a = array[2] = 3
        [3,4] = [3,4] + 2 + 3 = [3,4,5]
    finished iterating:
        return [3,4,5]    


"""


def check_if_element_in_array_can_be_divided_by_number(array, number) -> list[bool]:
    """
    Check if element in array can be divided by number
    Use for loop
    """
    new_array = []
    for elements in array: # array = [1,2,3]
        if elements % number == 0: # a = 1, number = 2
            new_array.append(True)
        else:
            new_array.append(False)    

    return new_array
"""
    first iteration:
        elements = array[0] # here elements is equal to the index of array, so elements = 1
        if 1 % 2 = 0 != True
            [] = [] + False = [False] #since the 1 mod 2 does not equal 0, the boolean value False will be appended to the array.
    second iteration:
        elements = array[1] = elements = 2
        if 2 % 2 = 0 = True
            [False] = [False] + True = [False, True]
    third iteration:
        elements = array[2] = elements  = 3
        if 3 % 2 = 0 != True
            [False, True] = [False, True] + False = [False, True, False]
    finished iterating:
        return [False, True, False]              


"""            


def find_elements_that_contains_letter(array, condition) -> list:
    """
    Find elements that match condition
    Use for loop
    """
    new_array = []
    for elements in array: # array = ["Merca", "Jane", "John"]
        if elements.lower().find(condition) != -1: # a = "Merca", condtion = "e"
            new_array.append(elements)    
    return new_array       
"""
    first iteration:
        elements.lower = array[0] and converts "Merca" to lowercase
        merca.find("e") = 1
        if 1 != -1 = True
            [] = [] + "Merca" = ["Merca"] # append = array[array.lenght] = array.lenght = 0
    second iteration:
        elements.lower = array[1] and converts "Jane" to lowercase
        jane.find("e") = 3
        if 3 != -1 = True
            ["Merca"] = ["Merca"] + "Jane" = ["Merca", "Jane"] # array.lenght = 1 
    third iteration:
        elements.lower = array[2] and converts "John" to lowercase
        john.find("e") = -1   
        if -1 != -1 = False

    finished iterating:
        return ["Merca", "Jane"]         
"""    

def reverce_string(input_string):
    """
    Reverce string
    Use for loop
    """
    reverse_string = ""
    for letter in input_string: # input_string = "Merca", letter = "M"
        reverse_string = letter + reverse_string # 
    return reverse_string   
    """
        first iteration:
            "" = M + ""
        second iteration:
            M = e + M
        third iteration:
            eM = r + eM
        fourth iteration:
            reM = c + reM
        fifth iteration:
            crem = a + creM
        return statement:
            acreM         

    """