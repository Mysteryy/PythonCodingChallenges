import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 6]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    # New tests
    def test2_single_digit_non_nine(self):
        solution = Solution()
        input_a = [5]
        expected_output = [6]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test3_single_digit_nine(self):
        solution = Solution()
        input_a = [9]
        expected_output = [1, 0]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test4_all_nines(self):
        solution = Solution()
        input_a = [9, 9, 9]
        expected_output = [1, 0, 0, 0]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test5_large_number_no_carry(self):
        solution = Solution()
        input_a = [1, 2, 3, 8]
        expected_output = [1, 2, 3, 9]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test6_large_number_with_carry(self):
        solution = Solution()
        input_a = [2, 9, 9]
        expected_output = [3, 0, 0]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test7_all_zeroes(self):
        solution = Solution()
        input_a = [0]
        expected_output = [1]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test8_long_list_of_nines(self):
        solution = Solution()
        input_a = [9] * 100  # 100-digit number, all nines
        expected_output = [1] + [0] * 100
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test9_alternating_nine_and_non_nine(self):
        solution = Solution()
        input_a = [1, 9, 9, 8]
        expected_output = [1, 9, 9, 9]
        self.assertEqual(solution.plusOne(input_a), expected_output)

    def test10_trailing_zeroes(self):
        solution = Solution()
        input_a = [1, 0, 0, 9]
        expected_output = [1, 0, 1, 0]
        self.assertEqual(solution.plusOne(input_a), expected_output)
