import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "11"
        input_b = "1"
        expected_output = "100"
        self.assertEqual(solution.addBinary(input_a, input_b), expected_output)
