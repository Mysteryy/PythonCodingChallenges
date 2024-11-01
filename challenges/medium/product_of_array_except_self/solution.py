from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: First we will get the total product of the array, and count the number of 0s
        # Note that we exclude 0 from our product calculation and count 0s separately
        total_product = 1
        num_zeros = 0
        for x in nums:
            if x != 0:
                total_product *= x
            else:
                num_zeros += 1

        # Step 2: Next we will build a list of results for each number in nums
        result = []
        for num in nums:
            # If there are no 0s in the input list, the product is simply the total product / current num
            if num_zeros == 0:
                result.append(int(total_product / num))
            # Else if there is (1) 0, and it's this number, the product will be the total product excluding 0s
            elif num_zeros == 1 and num == 0:
                result.append(total_product)
            # Else there are either >1 0s, or there is 1 zero and it's not this number, making the result 0
            else:
                result.append(0)

        return result
