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