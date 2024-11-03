from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return

        i, j = 0, 0
        while j < len(nums):
            current_i = nums[i]
            current_j = nums[j]

            if current_i == 0 and current_j != 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 0:
                i += 1
            j += 1
