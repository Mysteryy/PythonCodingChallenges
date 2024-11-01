import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 4, 5]
        expected_output = True
        self.assertEqual(solution.increasingTriplet(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [5, 4, 3, 2, 1]
        expected_output = False
        self.assertEqual(solution.increasingTriplet(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = [2, 1, 5, 0, 4, 6]
        expected_output = True
        self.assertEqual(solution.increasingTriplet(input_a), expected_output)

    def test4(self):
        solution = Solution()
        input_a = [20, 100, 10, 12, 5, 13]
        expected_output = True
        self.assertEqual(solution.increasingTriplet(input_a), expected_output)
