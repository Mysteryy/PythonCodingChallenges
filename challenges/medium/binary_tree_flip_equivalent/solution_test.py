import unittest
from .solution import Solution, TreeNode


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
        input_b = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test2(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
        input_b = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))))
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test3(self):
        solution = Solution()
        input_a = TreeNode(1)
        input_b = TreeNode(1)
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test4(self):
        solution = Solution()
        input_a = TreeNode(2)
        input_b = TreeNode(1)
        self.assertFalse(solution.flipEquiv(input_a, input_b))

    def test5(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
        input_b = TreeNode(1, TreeNode(3, TreeNode(6)), TreeNode(2, TreeNode(5, TreeNode(8), TreeNode(7)), TreeNode(4)))
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test6(self):
        solution = Solution()
        input_a = TreeNode(1)
        input_b = TreeNode(1)
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test7(self):
        solution = Solution()
        input_a = TreeNode(1)
        input_b = TreeNode(2)
        self.assertFalse(solution.flipEquiv(input_a, input_b))

    def test8(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2), TreeNode(3))
        input_b = None
        self.assertFalse(solution.flipEquiv(input_a, input_b))

    def test9(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        input_b = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertTrue(solution.flipEquiv(input_a, input_b))

    def test10(self):
        solution = Solution()
        input_a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        input_b = TreeNode(1, TreeNode(3, TreeNode(7), TreeNode(6)), TreeNode(2, TreeNode(5), TreeNode(4)))
        self.assertTrue(solution.flipEquiv(input_a, input_b))
