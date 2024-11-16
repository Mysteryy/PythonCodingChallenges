import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = 2
        expected_output = 2
        self.assertEqual(solution.climbStairs(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = 3
        expected_output = 3
        self.assertEqual(solution.climbStairs(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = 4
        expected_output = 5
        self.assertEqual(solution.climbStairs(input_a), expected_output)
