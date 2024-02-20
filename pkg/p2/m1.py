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