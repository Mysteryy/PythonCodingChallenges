import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 4]
        input_b = 5
        expected_output = 2
        self.assertEqual(solution.maxOperations(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [3, 1, 3, 4, 3]
        input_b = 6
        expected_output = 1
        self.assertEqual(solution.maxOperations(input_a, input_b), expected_output)
