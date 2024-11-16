import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [0, 1, 0, 3, 12]
        expected_output = [1, 3, 12, 0, 0]
        solution.moveZeroes(input_a)
        self.assertListEqual(input_a, expected_output)

    def test2(self):
        solution = Solution()
        input_a = [0]
        expected_output = [0]
        solution.moveZeroes(input_a)
        self.assertListEqual(input_a, expected_output)

    def test3(self):
        solution = Solution()
        input_a = [2, 1]
        expected_output = [2, 1]
        solution.moveZeroes(input_a)
        self.assertListEqual(input_a, expected_output)
