import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = 121
        expected_output = True
        self.assertEqual(solution.isPalindrome(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = -121
        expected_output = False
        self.assertEqual(solution.isPalindrome(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = 10
        expected_output = False
        self.assertEqual(solution.isPalindrome(input_a), expected_output)
