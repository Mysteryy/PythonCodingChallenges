import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "abc"
        input_b = "ahbgdc"
        expected_output = True
        self.assertEqual(solution.isSubsequence(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "axc"
        input_b = "ahbgdc"
        expected_output = False
        self.assertEqual(solution.isSubsequence(input_a, input_b), expected_output)
