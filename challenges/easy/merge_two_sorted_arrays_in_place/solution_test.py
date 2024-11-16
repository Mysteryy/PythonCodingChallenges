import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 0, 0, 0]
        input_b = [2, 5, 6]
        expected_output = [1, 2, 2, 3, 5, 6]
        solution.merge(input_a, len(input_a) - len(input_b), input_b, len(input_b))
        self.assertListEqual(input_a, expected_output)

    def test2(self):
        solution = Solution()
        input_a = [4, 5, 6, 0, 0, 0]
        input_b = [1, 2, 3]
        expected_output = [1, 2, 3, 4, 5, 6]
        solution.merge(input_a, len(input_a) - len(input_b), input_b, len(input_b))
        self.assertListEqual(input_a, expected_output)

    def test3(self):
        solution = Solution()
        input_a = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
        input_b = [1, 2, 2]
        expected_output = [-1, 0, 0, 1, 2, 2, 3, 3, 3]
        solution.merge(input_a, len(input_a) - len(input_b), input_b, len(input_b))
        self.assertListEqual(input_a, expected_output)
