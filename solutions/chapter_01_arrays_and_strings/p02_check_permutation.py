"""
Chapter 1, Problem 2 - Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest
from collections import Counter


# Sorting solution: O(N*log(N))
def is_permutation_by_sort(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    return a_sorted == b_sorted


# Pythonic solution:  # TODO: check big O
def is_permutation_pythonic(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


# Counting solution: O(N)
def is_permutation_by_count(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    # Assume extended ASCII (256 characters)
    count_array = [0] * 256
    for char in a:
        count_array[ord(char)] += 1
    for char in b:
        if count_array[ord(char)] == 0:
            return False
        count_array[ord(char)] -= 1
    return True


# Test solutions
class Test(unittest.TestCase):

    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    expected_results = [test_case[2] for test_case in test_cases]

    def test_is_permutation_by_sort(self):
        results = []
        for test_case in self.test_cases:
            results.append(is_permutation_by_sort(test_case[0], test_case[1]))
        self.assertEqual(results, self.expected_results)

    def test_is_permutation_pythonic(self):
        results = []
        for test_case in self.test_cases:
            results.append(is_permutation_by_sort(test_case[0], test_case[1]))
        self.assertEqual(results, self.expected_results)

    def test_is_permutation_by_count(self):
        results = []
        for test_case in self.test_cases:
            results.append(is_permutation_by_sort(test_case[0], test_case[1]))
        self.assertEqual(results, self.expected_results)


if __name__ == "__main__":
    unittest.main()
