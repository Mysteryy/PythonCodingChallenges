from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_height = height[left]
            right_height = height[right]

            max_value = max(max_value, (right - left) * (min(left_height, right_height)))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_value
