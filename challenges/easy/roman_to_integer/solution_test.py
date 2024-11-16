import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = 'III'
        expected_output = 3
        self.assertEqual(solution.solution(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = 'LVIII'
        expected_output = 58
        self.assertEqual(solution.solution(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = 'MCMXCIV'
        expected_output = 1994
        self.assertEqual(solution.solution(input_a), expected_output)

    def test4(self):
        solution = Solution()
        input_a = 'IX'
        expected_output = 9
        self.assertEqual(solution.solution(input_a), expected_output)

    def test5(self):
        solution = Solution()
        input_a = 'XL'
        expected_output = 40
        self.assertEqual(solution.solution(input_a), expected_output)

    def test6(self):
        solution = Solution()
        input_a = 'CD'
        expected_output = 400
        self.assertEqual(solution.solution(input_a), expected_output)

    def test7(self):
        solution = Solution()
        input_a = 'XLABC'
        expected_output = 0
        self.assertEqual(solution.solution(input_a), expected_output)
