import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = "Hello World"
        expected_output = 5
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test2(self):
        solution = Solution()
        input_a = "SingleWord"
        expected_output = 10
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test3(self):
        solution = Solution()
        input_a = "  Leading and trailing spaces   "
        expected_output = 6
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test4(self):
        solution = Solution()
        input_a = "Short sentence."
        expected_output = 9
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test5(self):
        solution = Solution()
        input_a = "Words separated   by   multiple spaces"
        expected_output = 6
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test6(self):
        solution = Solution()
        input_a = "Another test with more words"
        expected_output = 5
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test7(self):
        solution = Solution()
        input_a = "Ending with a number 1234"
        expected_output = 4
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test8(self):
        solution = Solution()
        input_a = "  thi is 123 another kind of test for testing things where things are being tested."
        expected_output = 7
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test9(self):
        solution = Solution()
        input_a = "Uppercase WORD"
        expected_output = 4
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test10(self):
        solution = Solution()
        input_a = "Empty string test"
        expected_output = 4
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test11(self):
        solution = Solution()
        input_a = " "
        expected_output = 0
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test12(self):
        solution = Solution()
        input_a = "Ends with punctuation!"
        expected_output = 12
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test13(self):
        solution = Solution()
        input_a = "the final count downnnnn"
        expected_output = 8
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test14(self):
        solution = Solution()
        input_a = "1234567890 numbers in a sentence"
        expected_output = 8
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test15(self):
        solution = Solution()
        input_a = "Ends with symbols #@!"
        expected_output = 3
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test16(self):
        solution = Solution()
        input_a = "A"
        expected_output = 1
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test17(self):
        solution = Solution()
        input_a = "Two words"
        expected_output = 5
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test18(self):
        solution = Solution()
        input_a = "Multiple short words"
        expected_output = 5
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test19(self):
        solution = Solution()
        input_a = "Trailing spaces   "
        expected_output = 6
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)

    def test20(self):
        solution = Solution()
        input_a = ""
        expected_output = 0
        self.assertEqual(solution.lengthOfLastWord(input_a), expected_output)