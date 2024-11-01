import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertCountEqual(solution.productExceptSelf(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        self.assertCountEqual(solution.productExceptSelf(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = [0, 1, 0, -3, 3]
        expected_output = [0, 0, 0, 0, 0]
        self.assertCountEqual(solution.productExceptSelf(input_a), expected_output)
