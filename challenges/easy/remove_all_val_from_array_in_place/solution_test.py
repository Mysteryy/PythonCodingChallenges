import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2]
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(sorted(nums[:k]), sorted(expected))

    def test2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 1, 3, 0, 4]
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(sorted(nums[:k]), sorted(expected))

    def test3(self):
        nums = []
        val = 0
        expected = []
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(nums[:k], expected)

    def test4(self):
        nums = [1, 1, 1, 1]
        val = 1
        expected = []
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(nums[:k], expected)

    def test5(self):
        nums = [4, 5, 6, 7]
        val = 5
        expected = [4, 6, 7]
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(sorted(nums[:k]), sorted(expected))

    def test6(self):
        nums = [3, 3]
        val = 3
        expected = []
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, len(expected))
        self.assertEqual(sorted(nums[:k]), sorted(expected))
