import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [2, 3, 5, 1, 3]
        input_b = 3
        expected_output = [True, True, True, False, True]
        self.assertCountEqual(solution.kidsWithCandies(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [4, 2, 1, 1, 2]
        input_b = 1
        expected_output = [True, False, False, False, False]
        self.assertCountEqual(solution.kidsWithCandies(input_a, input_b), expected_output)

    def test3(self):
        solution = Solution()
        input_a = [12, 1, 12]
        input_b = 10
        expected_output = [True, False, True]
        self.assertCountEqual(solution.kidsWithCandies(input_a, input_b), expected_output)
