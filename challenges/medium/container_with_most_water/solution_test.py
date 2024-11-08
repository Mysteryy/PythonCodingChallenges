import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected_output = 49
        self.assertEqual(solution.maxArea(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [1, 1]
        expected_output = 1
        self.assertEqual(solution.maxArea(input_a), expected_output)
