from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Find the index where it belongs using a binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
