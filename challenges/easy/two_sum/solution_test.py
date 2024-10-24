import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_nums = [2, 7, 11, 15]
        input_target = 9
        expected_output = [0, 1]
        self.assertCountEqual(solution.twoSum(input_nums, input_target), expected_output)

    def test2(self):
        solution = Solution()
        input_nums = [3, 2, 4]
        input_target = 6
        expected_output = [1, 2]
        self.assertCountEqual(solution.twoSum(input_nums, input_target), expected_output)

    def test3(self):
        solution = Solution()
        input_nums = [3, 3]
        input_target = 6
        expected_output = [0, 1]
        self.assertCountEqual(solution.twoSum(input_nums, input_target), expected_output)

