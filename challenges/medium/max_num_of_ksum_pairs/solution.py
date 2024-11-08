from typing import List


class Solution:
    # There are at least 2 logical ways to solve this problem.
    # 1) Copy all nums less than k to a tmp list, and sort the list. Then use 2 pointer solution to count.
    # 2) Use a hash map to keep track of the unused values while looking for the difference required.
    #
    # This solution focuses on 2.
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = {}
        counter = 0

        for num in nums:
            diff = k - num
            if diff in cache and cache[diff] > 0:
                counter += 1
                cache[diff] -= 1
            else:
                cache[num] = (1 if num not in cache else cache[num] + 1)

        return counter
