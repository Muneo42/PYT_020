# def concatenate_binary(int_list):
#     binary_string = ""
#     for num in int_list:
#         if num == 0:
#             binary_string += '0'
#         else:
#             binary_string += bin(num)[2:]  # Using built-in function bin() to get binary representation
#     return binary_string

# # Example usage:
# numbers = [42, 7, 128, 255]
# concatenated_binary = concatenate_binary(numbers)
# print(f"The concatenated binary representation of {numbers} is: {concatenated_binary}")

# def int_to_bin(int_list):
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
#         binary = binary.zfill(8)
#         binary_list.append(binary)
#     return binary_list

# # Example usage:
# numbers = [42, 7, 128, 255]
# binary_representations = int_to_bin(numbers)
# print(f"The binary representations of {numbers} (padded to 8 bits) are: {binary_representations}")

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
        # Separate the binary string into chunks of 6 bits
        for i in range(0, len(binary), 6):
            chunk = binary[i:i+6]
            # Pad the last chunk with zeros if its length is less than 6
            chunk = chunk.ljust(6, '0')
            binary_list.append(chunk)
    return binary_list

# Example usage:
numbers = [42, 7, 128, 255]
binary_representations = int_to_bin(numbers)
print(f"The binary representations of {numbers} (separated into chunks of 6 bits) are: {binary_representations}")
