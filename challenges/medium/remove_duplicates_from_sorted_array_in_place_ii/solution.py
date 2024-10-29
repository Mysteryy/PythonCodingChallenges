from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            element = nums[i]
            if element != nums[k - 2]:
                nums[k] = element
                k += 1

        return k
