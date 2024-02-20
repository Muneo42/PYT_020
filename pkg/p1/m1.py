def cast_string_to_list(s):
    """Split a string into a list (Step 1)

    Example:
        "ABCDE" returns ['A','B','C','D','E']

    Args:
        s (str): The string to be split
    Returns:
        A list of the characters
    """
    return list(s)


def cast_elements_to_integers(lst):
    """Cast every character to integers (Step 2)

    Example: ['A','B','C','D','E'] returns [65,66,67,68,69]

    Args:
        lst (list): The list of characters to be cast

    Returns:
         A list of integers
    """
    return [ord(i) for i in lst]


def cast_elements_to_binaries(lst):
    """Cast every integer to binary digits (Step 3)

    Example: [65,66] returns ['1000001','1000010']

    Args:
        lst (list): The list of integers to be cast

    Returns:
         A list of binary represented characters
    """
    return [bin(i)[2:] for i in lst]


def justify_elements(lst):
    """Right justify each element on 8 positions with zeros (Step 4)

    Args:
        lst (List of str):
            List of the justified elements

    Returns:
        List of the justified elements

    """
    # l = []
    # for element in lst:
    #     element = element.zfill(8)
    #     l.append(element)

    return [element.zfill(8) for element in lst]


def lst_to_str(lst):
    """Transform a list of strings to a string (Step 5)

    Args:
        lst (List): A list of strings (binary digits)

    Returns:
        String (binary digits)
    """
    # s = ""
    # for element in lst:
    #     s = s + element

    return ''.join(lst)