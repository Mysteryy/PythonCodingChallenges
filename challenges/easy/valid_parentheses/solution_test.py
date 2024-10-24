import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = '()'
        self.assertTrue(solution.isValid(input_a))

    def test2(self):
        solution = Solution()
        input_a = '()[]{}'
        self.assertTrue(solution.isValid(input_a))

    def test3(self):
        solution = Solution()
        input_a = '(]}{'
        self.assertFalse(solution.isValid(input_a))

    def test4(self):
        solution = Solution()
        input_a = '([])'
        self.assertTrue(solution.isValid(input_a))

    def test5(self):
        solution = Solution()
        input_a = '}{'
        self.assertFalse(solution.isValid(input_a))

    def test6(self):
        solution = Solution()
        input_a = '{}()()()()[][]{}[]{}()()()()()[][]{}[]{[()]}()()()()()[][]{}[]{}()()()()()[][]{}[]{}()()()()()[][]{}[]{}()'
        self.assertTrue(solution.isValid(input_a))

    def test7(self):
        solution = Solution()
        input_a = '(((((([][{}{{}}]))))))'
        self.assertTrue(solution.isValid(input_a))

    def test8(self):
        solution = Solution()
        input_a = '(((((([][{}{{}}]))))'
        self.assertFalse(solution.isValid(input_a))

    def test9(self):
        solution = Solution()
        input_a = '(((((([]A[{}{{}}]))))'
        self.assertFalse(solution.isValid(input_a))
