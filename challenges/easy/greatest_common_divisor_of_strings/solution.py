from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Get the numerical gcd of both lists
        greatest_cd = gcd(len(str1), len(str2))
        # Sanity checks, there is no gcd string if these conditions are not met
        if not str1 or not str2 or (str1 + str2 != str2 + str1):
            return ''
        # The gcd string is the substr of either string from 0 to the numerical gcd
        return str1[0:greatest_cd]
