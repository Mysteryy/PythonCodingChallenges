import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [1, 3, 5, 6]
        input_b = 5
        expected_output = 2
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [1, 3, 5, 6]
        input_b = 2
        expected_output = 1
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test3(self):
        solution = Solution()
        input_a = [1, 3, 5, 6]
        input_b = 7
        expected_output = 4
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test4(self):
        solution = Solution()
        input_a = [1, 3, 5, 6]
        input_b = 0
        expected_output = 0
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test5(self):
        solution = Solution()
        input_a = [1, 3, 5, 6]
        input_b = 3
        expected_output = 1
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test6(self):
        solution = Solution()
        input_a = [10, 20, 30, 40, 50]
        input_b = 25
        expected_output = 2
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test7(self):
        solution = Solution()
        input_a = [10, 20, 30, 40, 50]
        input_b = 10
        expected_output = 0
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test8(self):
        solution = Solution()
        input_a = [5, 15, 25, 35, 45]
        input_b = 50
        expected_output = 5
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test9(self):
        solution = Solution()
        input_a = [5, 15, 25, 35, 45]
        input_b = 5
        expected_output = 0
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test10(self):
        solution = Solution()
        input_a = [1]
        input_b = 0
        expected_output = 0
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test11(self):
        solution = Solution()
        input_a = []
        input_b = 5
        expected_output = 0  # Since the list is empty, the target should be inserted at index 0
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test12(self):
        solution = Solution()
        input_a = list(range(1, 101))  # Generates a list from 1 to 100
        input_b = 50
        expected_output = 49  # Target is in the middle of the list
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)

    def test13(self):
        solution = Solution()
        input_a = list(range(1, 201, 2))  # Generates a list of odd numbers from 1 to 199
        input_b = 100
        expected_output = 50  # Target should be inserted in the middle
        self.assertEqual(solution.searchInsert(input_a, input_b), expected_output)
