"""
Chapter N: Problem M - <Problem name>

<Problem description>
"""

import unittest

# Solution functions
def foo():
    pass


# Tests
class Test(unittest.TestCase):
    test_cases = []
    test_funcs = []

    # Tests funcs here
    def test_solution(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for test in test_cases:
                for func in test_funcs:
                    start = time.perf_counter()
                    pass
                    # Assertions here
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
