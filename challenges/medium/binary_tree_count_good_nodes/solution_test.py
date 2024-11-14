import unittest
from solution import Solution, TreeNode


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = TreeNode(3,
                           TreeNode(1, TreeNode(3)),
                           TreeNode(4, TreeNode(1), TreeNode(5)))
        expected_output = 4
        self.assertEqual(solution.goodNodes(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
        expected_output = 3
        self.assertEqual(solution.goodNodes(input_a), expected_output)
