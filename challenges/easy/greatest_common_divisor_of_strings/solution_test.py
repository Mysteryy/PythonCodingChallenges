import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "ABCABC"
        input_b = "ABC"
        expected_output = "ABC"
        self.assertEqual(solution.gcdOfStrings(input_a, input_b), expected_output)


    def test2(self):
        solution = Solution()
        input_a = "ABABAB"
        input_b = "ABAB"
        expected_output = "AB"
        self.assertEqual(solution.gcdOfStrings(input_a, input_b), expected_output)


    def test3(self):
        solution = Solution()
        input_a = "LEET"
        input_b = "CODE"
        expected_output = ""
        self.assertEqual(solution.gcdOfStrings(input_a, input_b), expected_output)
