import unittest
from .solution import Solution, TreeNode


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = TreeNode(3,
                           TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                           TreeNode(1, TreeNode(9), TreeNode(8)))
        input_b = TreeNode(3,
                           TreeNode(5, TreeNode(6), TreeNode(7)),
                           TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
        expected_output = True
        self.assertEqual(solution.leafSimilar(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2), TreeNode(3))
        input_b = TreeNode(1, TreeNode(3), TreeNode(2))
        expected_output = False
        self.assertEqual(solution.leafSimilar(input_a, input_b), expected_output)
