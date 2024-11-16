import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "abc"
        input_b = "pqr"
        expected_output = "apbqcr"
        self.assertEqual(solution.mergeAlternately(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "ab"
        input_b = "pqrs"
        expected_output = "apbqrs"
        self.assertEqual(solution.mergeAlternately(input_a, input_b), expected_output)

    def test3(self):
        solution = Solution()
        input_a = "abcd"
        input_b = "pq"
        expected_output = "apbqcd"
        self.assertEqual(solution.mergeAlternately(input_a, input_b), expected_output)

