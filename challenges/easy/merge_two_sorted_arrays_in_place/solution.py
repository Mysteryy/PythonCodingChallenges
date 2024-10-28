from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            current_1 = nums1[j] if j >= 0 else None
            current_2 = nums2[k] if k >= 0 else None

            if current_1 is not None and current_2 is not None:
                selected = current_1 if current_1 >= current_2 else current_2
            else:
                selected = current_1 if current_1 is not None else current_2

            nums1[i] = selected

            if selected == current_1:
                j -= 1
            else:
                k -= 1
