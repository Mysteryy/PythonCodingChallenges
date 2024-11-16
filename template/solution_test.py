import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = []
        expected_output = [0, 1]
        self.assertCountEqual(solution.solution(input_a), expected_output)
