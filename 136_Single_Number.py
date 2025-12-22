from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for x in nums:
            unique ^= x

        return unique