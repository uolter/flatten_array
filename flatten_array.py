

def flatten(input_list):
    """ Return a flatten list given a nested one.
    
    :param input_list: list of numbers of list of list of numbers
    """

    result_list = []
    
    for e in input_list:
        if isinstance(e, int):
            result_list.append(e)
        elif isinstance(e, list):
            result_list += flatten(e)
    
    return result_list