"""
Chapter 1, Problem 3 - URLify

Write a method to replace all spaces in a string with "%20": You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
"""
import unittest


# References

# https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640
# https://quastor.org/cracking-the-coding-interview/arrays-and-strings/urlify


def urlify_pythonic_split_and_join(a: str) -> str:
    return "%20".join(a.split())


def urlify_pythonic_replace(a: str, length: int) -> str:
    return str[:length].replace(" ", "%20")



def urlify_two_pointer(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    pass


class Test(unittest.TestCase):

    test_cases = (
        ("www.google.com", 14, "www.google.com"),
        ("This is a test", 14, "This%20is%20a%20test"),
        ("This is  another   test", 20, "This%20is%20another%20test"),
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
        ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
        (" a b    ", 4, "%20a%20b"),
        (" a b       ", 5, "%20a%20b%20"),
    )

    def test_urlify_pythonic_split_and_join(self):
        for test_case in self.test_cases:
            self.assertEqual(urlify_pythonic_split_and_join(test_case[0]), test_case[2])


if __name__ == "__main__":
    unittest.main()