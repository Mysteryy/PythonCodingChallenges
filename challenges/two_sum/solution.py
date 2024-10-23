# LeetCode #1 - Two Sum
#
# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.
#
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use a cache for faster lookup of compliment values
        cache = {}

        # Iterate all elements in nums
        for i, num_a in enumerate(nums):
            # Calculate the complement needed to sum to target
            complement = target - num_a
            if complement in cache:
                return i, cache[complement]
            cache[num_a] = i

