# !/usr/bin/env python3

"""Small presentation helpers."""


# A function to convert bytes into human readable sizes
def convert_bytes(size):

    """ A function to convert bytes into human readable sizes. """

    # Declare variables
    suffix = 0  # Iterator variable for the suffix index
    suffixes = ["B", "KB", "MB", "GB", "TB"]  # Suffixes

    # Loop and divide
    while size > 1024:
        suffix += 1 # Increment the index of the suffix
        size = size / 1024 # Apply the division

    # Calculate final output size
    size = str(round(size, 2)) + chr(32) + suffixes[suffix]

    return size
