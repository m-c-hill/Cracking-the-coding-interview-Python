"""
Chapter 1: Problem 1 - Is Unique

Implement an algorithm to determine if a string has all unique characters.
Extension: What if you cannot use additional data structures?
"""
import unittest


def is_unique_algorithmic(string: str) -> bool:
    """
    Assume the string is composed of ASCII characters (128 total). Convert each character to
    unicode integer using ord() and create a boolean array of length 128. Loop through string
    and set booleans accordingly.
    """
    if len(string) > 128:
        return False

    unicode_chars_in_string = [False] * 128
    for char in string:
        char_unicode = ord(char)
        if unicode_chars_in_string[char_unicode]:
            return False
        unicode_chars_in_string[char_unicode] = True
    return True


# Use sets to track characters used in the string while looping through the string.
def is_unique_using_sets(string: str) -> bool:
    characters = set()
    for char in string.lower():
        if char in characters:
            return False
        characters.add(char)
    return True


# Pythonic solution using sets to compare length.
def is_unique_set_length(string: str) -> bool:
    return len(set(string)) == len(string)


# Create an ordered list from string and compare each character to the character which proceeds it.
def is_unique_sorting(string: str) -> bool:
    string = sorted(string)
    prev_char = ""
    for char in string:
        if char == prev_char:
            return False
        prev_char = char
    return True


class Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
