from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            elif n > second:
                return True

        return False
