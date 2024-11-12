import unittest
from solution import Solution, TreeNode


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected_output = 3
        self.assertEqual(solution.maxDepth(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = TreeNode(2, right=TreeNode(2))
        expected_output = 2
        self.assertEqual(solution.maxDepth(input_a), expected_output)
