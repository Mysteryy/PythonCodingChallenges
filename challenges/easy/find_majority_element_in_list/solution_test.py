import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [3, 2, 3]
        expected_output = 3
        self.assertEqual(solution.majorityElement(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [2, 2, 1, 1, 1, 2, 2]
        expected_output = 2
        self.assertEqual(solution.majorityElement(input_a), expected_output)
