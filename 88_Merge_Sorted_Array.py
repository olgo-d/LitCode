from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x1, x2, position_add = m-1, n-1, n+m - 1
        while x2 >= 0:
            if x1 >= 0 and nums1[x1] > nums2[x2]:
                nums1[position_add] = nums1[x1]
                x1 -= 1
            else:
                nums1[position_add] = nums2[x2]
                x2 -= 1

            position_add -= 1