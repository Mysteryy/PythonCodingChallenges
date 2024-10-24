import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        nums = [1, 1, 2]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test2(self):
        solution = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test3(self):
        solution = Solution()
        nums = [1]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test4(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test5(self):
        solution = Solution()
        nums = [2, 2, 2, 2, 2]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [2])