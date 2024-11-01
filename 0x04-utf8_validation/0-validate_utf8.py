#!/usr/bin/python3

"""
a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0

    # Masks to check the byte patterns
    mask1 = 0b10000000  # 128 in decimal
    mask2 = 0b11000000  # 192 in decimal

    for byte in data:
        if num_bytes == 0:
           
            if (byte & 0b10000000) == 0:
                continue  # 1-byte character
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1  # 2-byte character
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2  # 3-byte character
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8

        else:
            # Check if byte is a continuation byte (starts with '10')
            if (byte & mask2) != mask1:
                return False
            num_bytes -= 1

    
    return num_bytes == 0
