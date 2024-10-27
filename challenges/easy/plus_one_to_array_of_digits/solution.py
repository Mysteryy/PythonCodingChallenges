from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        # Iterate the list backwards
        for i in range(len(digits) - 1, -1, -1):
            # If digit is less than 9, we don't have any carry over so just add 1 and return, we are done
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:  # Else this sum was 10 so we have 0 in the ith place, and carry the 1 next time
                digits[i] = 0

        # If the code makes it here without returning, we had carryover left so insert a 1 at the beginning
        digits.insert(0, 1)
        return digits
