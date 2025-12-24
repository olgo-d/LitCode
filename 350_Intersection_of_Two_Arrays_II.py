from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_seen = {}
        result = []

        for x in nums1:
            if x in count_seen:
                count_seen[x] += 1
            else:
                count_seen[x] = 1

        for x in nums2:
            if x in count_seen and count_seen[x] != 0:
                result.append(x)
                count_seen[x] -= 1

        return result