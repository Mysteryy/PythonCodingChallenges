import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        expected_output = 5, [1, 1, 2, 2, 3]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test2(self):
        solution = Solution()
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_output = 7, [0, 0, 1, 1, 2, 3, 3]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test3(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        expected_output = 5, [1, 2, 3, 4, 5]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test4(self):
        solution = Solution()
        nums = [1, 1, 1, 1, 1]
        expected_output = 2, [1, 1]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test5(self):
        solution = Solution()
        nums = [2, 2, 3, 3, 4, 4, 4, 5]
        expected_output = 7, [2, 2, 3, 3, 4, 4, 5]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test6(self):
        solution = Solution()
        nums = []
        expected_output = 0, []
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test7(self):
        solution = Solution()
        nums = [5, 5, 5, 5, 6, 6, 7, 7]
        expected_output = 6, [5, 5, 6, 6, 7, 7]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test8(self):
        solution = Solution()
        nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6]
        expected_output = 10, [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])

    def test9(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3, 3, 4, 4]
        expected_output = 8, [1, 1, 2, 2, 3, 3, 4, 4]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output[0])
        self.assertEqual(nums[:k], expected_output[1])
