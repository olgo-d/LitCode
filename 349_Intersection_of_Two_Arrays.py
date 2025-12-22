from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resalt = []
        dct = {}

        for num in nums1:
            if num not in dct:
                dct[num] = 1

        for num in nums2:
            if num in dct and dct[num] == 1:
                resalt.append(num)
                dct[num] = 2

        return resalt