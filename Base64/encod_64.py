''' Fonction to incode in base64 '''

def str_to_b64(input_str):
    """Transform a string to its base64 encoded representation
    
    Args:
        input_str (str): The input string to be encoded
        
    Returns:
        str: The base64 encoded string
    """
    # Convert input string to list of characters
    def string_to_list(s):
        return list(s)

    # Convert list of characters to list of ASCII values
    def char_to_int(lst):
        return [ord(char) for char in lst]

    # Convert list of ASCII values to list of binary strings
    def int_to_bin(int_list):
        return [bin(num)[2:].zfill(8) for num in int_list]

    # Convert list of binary strings to single binary string
    def bin_to_str(binary_list):
        return ''.join(binary_list)

    # Convert binary string to list of 6-bit binary strings
    def str_to_6bit(binary):
        binary_list = []
        for i in range(0, len(binary), 6):
            chunk = binary[i:i+6]
            chunk = chunk.ljust(6, '0')  # Pad the last chunk with zeros if its length is less than 6
            binary_list.append(chunk)
        return binary_list

    # Convert list of 6-bit binary strings to base64 encoded string
    def bit_to_b64(binary_list):
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        base64_encoded = ""
        for binary in binary_list:
            decimal = int(binary, 2)
            base64_encoded += base64_chars[decimal]

        padding = (4 - len(binary_list) % 4) % 4
        base64_encoded += '=' * padding

        return base64_encoded

    # Step 1: Convert string to list of characters
    characters = string_to_list(input_str)

    # Step 2: Convert characters to ASCII values
    ascii_values = char_to_int(characters)

    # Step 3: Convert ASCII values to binary strings
    binary_strings = int_to_bin(ascii_values)

    # Step 4: Concatenate binary strings
    binary_string = bin_to_str(binary_strings)

    # Step 5: Convert binary string to list of 6-bit binary strings
    six_bit_binary_list = str_to_6bit(binary_string)

    # Step 6: Convert list of 6-bit binary strings to base64 encoded string
    base64_encoded_string = bit_to_b64(six_bit_binary_list)

    return base64_encoded_string

def b64_to_str(base64_str):
    """Transform a base64 string back to its original string
    
    Args:
        base64_str (str): A base64 encoded string
        
    Returns:
        str: The decoded string
    """
    # The list of base64 characters
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Reverse lookup dictionary to get the decimal value from base64 character
    char_to_decimal = {char: index for index, char in enumerate(base64_chars)}

    # Remove padding '=' characters
    base64_str = base64_str.rstrip('=')

    # Convert base64 characters back to decimal values
    decimal_list = [char_to_decimal[char] for char in base64_str]

    # Convert decimal values to 6-bit binary strings
    binary_list = [bin(decimal)[2:].zfill(6) for decimal in decimal_list]

    # Concatenate binary strings
    binary_string = ''.join(binary_list)

    # Split binary string into 8-bit chunks
    eight_bit_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    # Convert each 8-bit binary chunk to its ASCII character representation
    ascii_characters = [chr(int(chunk, 2)) for chunk in eight_bit_chunks]

    # Join characters into a single string
    return ''.join(ascii_characters)

# Test the function
input_string = input("Please enter a string: ")
encoded_string = str_to_b64(input_string)
print("Base64 Encoded String:", encoded_string)

# Test the function
base64_input = input("Please enter a base64 string: ")
decoded_string = b64_to_str(base64_input)
print("Decoded String:", decoded_string)

# # Ask for a user input: 
# def string_to_list():
#     """Split a string into a list (Step 1)

#     Example:
#         "ABCDE" returns ['A','B','C','D','E']

#     Args:
#         s (str): The string to be split
#     Returns:
#         A list of the characters
#     """
#     user_input = input("Please enter some letters: ")
#     liste_transform = list(user_input)
#     return liste_transform

# # Convert the list of char into int if ascii table
# def char_to_int(input_str):
#     """Cast every character to integers (Step 2)

#     Example: ['A','B','C','D','E'] returns [65,66,67,68,69]

#     Args:
#         lst (list): The list of characters to be cast

#     Returns:
#          A list of integers
#     """
#     int_table = []
#     for char in input_str:
#         ascii_val = ord(char)
#         int_table.append(ascii_val)
#     return int_table

# # Convert integer into binary
# def int_to_bin(int_list):
#     """Cast every integer to binary digits (Step 3)

#     Example: [65,66] returns ['1000001','1000010']

#     Args:
#         lst (list): The list of integers to be cast

#     Returns:
#          A list of binary represented characters
#     """
#     binary_list = []
#     for num in int_list:
#         binary = ''
#         if num == 0:
#             binary = '0'
#         else:
#             while num > 0:
#                 binary = str(num % 2) + binary
#                 num //= 2
#         # Pad the binary string with leading zeros to ensure it is 8 bits long
#         """Right justify each element on 8 positions with zeros

#         Args:
#             lst (List of str):
#                 List of the justified elements

#         Returns:
#             List of the justified elements

#         """
#         binary = binary.zfill(8)
#         binary_list.append(binary)
#     return binary_list

# def bin_to_str(binary_list):
#     """Transform a list of strings to a string

#     Args:
#         lst (List): A list of strings (binary digits)

#     Returns:
#         String (binary digits)
#     """
#     binary_string = ""
#     for binary in binary_list:
#         binary_string += binary
#     return binary_string

# def str_to_6bit(binary):
#     """Transform a list of strings to a string of 6 bits

#     Args:
#         lst (List): A list of strings (binary digits)

#     Returns:
#         String formated in 6bits (binary digits)
#     """
#     binary_list = []
#     for i in range(0, len(binary), 6):
#             chunk = binary[i:i+6]
#             # Pad the last chunk with zeros if its length is less than 6
#             chunk = chunk.ljust(6, '0')
#             binary_list.append(chunk)
#     return binary_list

# def bit_to_b64(binary_list):
#     """Transform a list of 6bits string into a string of base64

#     Args:
#         lst (List): A list of strings (binary digits 6 bits)

#     Returns:
#         String (base64)
#     """
#     # The list of base64 character
#     base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     base64_encoded = ""
#     for binary in binary_list:
#         # Convert binary string to decimal integer
#         decimal = int(binary, 2)
#         # Map the decimal integer to its corresponding base64 character
#         base64_encoded += base64_chars[decimal]
    
#     # Calculate the number of padding '=' characters needed
#     padding = (4 - len(binary_list) % 4) % 4
#     # Add padding '=' characters
#     base64_encoded += '=' * padding
    
#     return base64_encoded

# def dec_to_b64():
#     variable = string_to_list()
#     variable = char_to_int(variable)
#     variable = int_to_bin(variable)
#     variable = bin_to_str(variable)
#     variable = str_to_6bit(variable)
#     print(bit_to_b64(variable))