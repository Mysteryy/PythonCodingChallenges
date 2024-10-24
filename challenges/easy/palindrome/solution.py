class Solution(object):
    def isPalindrome(self, x):
        """
        Note: This solution focuses on the most concise, Python specific implementation.
        :type x: int
        :rtype: bool
        """
        return x >= 0 and x == int(str(x)[::-1])
