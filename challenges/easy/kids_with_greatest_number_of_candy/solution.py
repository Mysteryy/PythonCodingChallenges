from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # First find the max value in the initial list
        max_initial = max(candies)
        # Now build up a list of boolean values where each value indicates that this would be >= initial_max
        return [num_candies + extraCandies >= max_initial for num_candies in candies]
