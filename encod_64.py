''' Fonction to incode in base64'''

# Ask for a user input: 
def string_to_list():
    user_input = input("Please enter some letters: ")
    liste_transform = list(user_input)
    return liste_transform

# Convert the list of char into int if ascii table
def char_to_int(input_str):
    int_table = []
    for char in input_str:
        ascii_val = ord(char)
        int_table.append(ascii_val)
    return int_table

# Convert integer into binary
def int_to_bin(int_list):
    binary_list = []
    for num in int_list:
        binary = ''
        if num == 0:
            binary = '0'
        else:
            while num > 0:
                binary = str(num % 2) + binary
                num //= 2
        # Pad the binary string with leading zeros to ensure it is 8 bits long
        binary = binary.zfill(8)
        binary_list.append(binary)
    return binary_list

def bin_to_str(binary_list):
    binary_string = ""
    for binary in binary_list:
        binary_string += binary
    return binary_string

def str_to_6bit(binary):
    binary_list = []
    for i in range(0, len(binary), 6):
            chunk = binary[i:i+6]
            # Pad the last chunk with zeros if its length is less than 6
            chunk = chunk.ljust(6, '0')
            binary_list.append(chunk)
    return binary_list

def bit_to_b64(binary_list):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_encoded = ""
    for binary in binary_list:
        # Convert binary string to decimal integer
        decimal = int(binary, 2)
        # Map the decimal integer to its corresponding base64 character
        base64_encoded += base64_chars[decimal]
    
    # Calculate the number of padding '=' characters needed
    padding = (4 - len(binary_list) % 4) % 4
    # Add padding '=' characters
    base64_encoded += '=' * padding
    
    return base64_encoded

variable = string_to_list()
variable = char_to_int(variable)
variable = int_to_bin(variable)
variable = bin_to_str(variable)
variable = str_to_6bit(variable)
print(bit_to_b64(variable))