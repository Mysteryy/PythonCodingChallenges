class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        new_str = ''
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                new_str += word1[i]
            if i < len(word2):
                new_str += word2[i]

            i += 1

        return new_str
