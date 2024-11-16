import unittest
from .solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = ["flower", "flow", "flight"]
        expected_output = "fl"
        self.assertEqual(solution.solution(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = ["dog", "racecar", "car"]
        expected_output = ""
        self.assertEqual(solution.solution(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = ["dog", "doggie", "potato"]
        expected_output = ""
        self.assertEqual(solution.solution(input_a), expected_output)

    def test4(self):
        solution = Solution()
        input_a = ["pop tart", "pomskie", "potato"]
        expected_output = "po"
        self.assertEqual(solution.solution(input_a), expected_output)

    def test5(self):
        solution = Solution()
        input_a = ["abcde", "abbcdefgh"]
        expected_output = "ab"
        self.assertEqual(solution.solution(input_a), expected_output)
