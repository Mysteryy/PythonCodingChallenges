import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "sadbutsad"
        input_b = "sad"
        expected_output = 0
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "hello"
        input_b = "ll"
        expected_output = 2
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)

    def test3(self):
        solution = Solution()
        input_a = "abcdef"
        input_b = "xyz"
        expected_output = -1  # Not found
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)

    def test4(self):
        solution = Solution()
        input_a = "mississippi"
        input_b = "iss"
        expected_output = 1
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)

    def test5(self):
        solution = Solution()
        input_a = "aabbcc"
        input_b = "bb"
        expected_output = 2
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)

    def test6(self):
        solution = Solution()
        input_a = "testcase"
        input_b = "case"
        expected_output = 4
        self.assertEqual(solution.strStr(input_a, input_b), expected_output)
