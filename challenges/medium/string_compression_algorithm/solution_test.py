import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = ["a", "a", "b", "b", "c", "c", "c"]
        expected_output = 6, ["a", "2", "b", "2", "c", "3"]
        self.assertEqual(solution.compress(input_a), expected_output[0])
        self.assertListEqual(input_a[0:expected_output[0]], expected_output[1])

    def test2(self):
        solution = Solution()
        input_a = ["a"]
        expected_output = 1, ["a"]
        self.assertEqual(solution.compress(input_a), expected_output[0])
        self.assertListEqual(input_a[0:expected_output[0]], expected_output[1])

    def test3(self):
        solution = Solution()
        input_a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected_output = 4, ["a", "b", "1", "2"]
        self.assertEqual(solution.compress(input_a), expected_output[0])
        self.assertListEqual(input_a[0:expected_output[0]], expected_output[1])

    def test4(self):
        solution = Solution()
        input_a = ["a", "b", "c"]
        expected_output = 3, ["a", "b", "c"]
        self.assertEqual(solution.compress(input_a), expected_output[0])
        self.assertListEqual(input_a[0:expected_output[0]], expected_output[1])
