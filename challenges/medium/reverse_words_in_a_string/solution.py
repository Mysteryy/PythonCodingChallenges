class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into a list and then reverse the list (split with no args removes extra white space)
        split_string = s.split()[::-1]
        # Join the reverser list of words back together using a single space and return it
        return ' '.join(split_string)
