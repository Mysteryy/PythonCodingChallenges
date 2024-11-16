import unittest
from .solution import Solution, TreeNode


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = TreeNode(5,
                           TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                           TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
                           )
        input_b = 22
        expected_output = True
        self.assertEqual(solution.hasPathSum(input_a, input_b), expected_output)

    def test2(self):
        solution = Solution()
        input_a = TreeNode(5,
                           TreeNode(2),
                           TreeNode(3)
                           )
        input_b = 5
        expected_output = False
        self.assertEqual(solution.hasPathSum(input_a, input_b), expected_output)

    def test3(self):
        solution = Solution()
        input_a = None
        input_b = 0
        expected_output = False
        self.assertEqual(solution.hasPathSum(input_a, input_b), expected_output)
