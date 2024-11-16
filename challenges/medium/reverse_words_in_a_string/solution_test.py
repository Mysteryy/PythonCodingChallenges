import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "the sky is blue"
        expected_output = "blue is sky the"
        self.assertEqual(solution.reverseWords(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "  hello world  "
        expected_output = "world hello"
        self.assertEqual(solution.reverseWords(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = "the sky is blue"
        expected_output = "blue is sky the"
        self.assertEqual(solution.reverseWords(input_a), expected_output)
