import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "abcde"
        input_b = "cdeab"
        expected_output = True
        self.assertEqual(solution.rotateString(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "abcde"
        input_b = "abced"
        expected_output = False
        self.assertEqual(solution.rotateString(input_a, input_b), expected_output)
