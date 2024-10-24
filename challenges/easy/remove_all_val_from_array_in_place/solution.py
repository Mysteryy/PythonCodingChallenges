from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        del nums[k:]  # Not required by the challenge, but makes for a nicer solution
        return k
