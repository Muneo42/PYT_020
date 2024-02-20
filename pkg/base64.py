def main():
    v = cast_string_to_list("ABCD")
    print(v)
    v = cast_elements_to_integers(v)
    print(v)
    v = cast_elements_to_binaries(v)
    print(v)
    v = justify_elements(v)
    print(v)
    v = lst_to_str(v)
    print(v)
    v = split_into_six(v)
    print(v)
    v = justify_last_block(v)
    print(v)
    v = cast_binaries_to_decimals(v)
    print(v)
    v = create_base64_list(v)
    print(v)
    v = create_base64_string(v)
    print(v)
    v = justify_base64_string(v)
    print(v)


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


def split_into_six(s):
    """Split string into block of 6 characters (Step 6)

    Args:
        s (str): The string to split into 6 character blocks

    Returns:
        The split string in a list
    """
    l = []
    nb_blocks = len(s) // 6
    if len(s) % 6 != 0:
        nb_blocks += 1
    for n in range(nb_blocks):
        l.append(s[n * 6:n * 6 + 6])
    return l


def justify_last_block(l):
    """Justify the last block of the list (step 7)

    Args:
        l (list): List containing the block to be justified

    Returns:
        The list with the last block justified
    """
    l[-1] = l[-1].ljust(6, '0')
    return l


def cast_binaries_to_decimals(l):
    """Cast the binary elements to decimal values (Step 8)

    Args:
        l (list of 6 bits binary representations):

    Returns:
        the updated list
    """
    for i in range(len(l)):
        l[i] = int(l[i], base=2)
    return l


def create_base64_list(l):
    """Create the base64 list (Step 9)

    Args:
        l (list): List of integers for base64 characters

    Returns:
         The list of base 64 characters
    """
    b64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in range(len(l)):
        l[i] = b64_table[l[i]]
    return l


def create_base64_string(l):
    """Create the base 64 string (Step 10)

    Args:
        l (list): List of base 64 characters

    Returns:
        The base 64 string
    """
    return ''.join(l)


def justify_base64_string(s):
    """Justify the base 64 string

    The final string length must be a multiple of 4

    Args:
        s (str): The string to justify

    Returns:
        The justified string
    """
    if len(s) % 4 != 0:
        s += '=' * (4 - len(s) % 4)
    return s


if __name__ == '__main__':
    main()
