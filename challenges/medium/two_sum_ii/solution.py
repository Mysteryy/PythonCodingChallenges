from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            num_a = numbers[start]
            num_b = numbers[end]
            current_sum = num_a + num_b

            if current_sum == target:
                return [start + 1, end + 1]
            elif current_sum > target:
                end -= 1
            elif current_sum < target:
                start += 1

        return []
