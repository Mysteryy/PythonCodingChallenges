from typing import List


class Solution:
    """
    This solution will use the Boyer–Moore majority vote algorithm to solve the problem.
    """

    def majorityElement(self, nums: List[int]) -> int:
        majority_element = None
        counter = 0
        for element in nums:
            if counter == 0:
                majority_element, counter = element, 1
            else:
                if element == majority_element:
                    counter += 1
                else:
                    counter -= 1

        return majority_element
