import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 4, 5, 6, 7]
        input_b = 3
        expected_output = [5, 6, 7, 1, 2, 3, 4]
        solution.rotate(input_a, input_b)
        self.assertListEqual(input_a, expected_output)

    def test2(self):
        solution = Solution()
        input_a = [-1, -100, 3, 99]
        input_b = 2
        expected_output = [3, 99, -1, -100]
        solution.rotate(input_a, input_b)
        self.assertListEqual(input_a, expected_output)
