from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for num in range(len(nums) + 1):
            result ^= num

        for num in nums:
            result ^= num

        return result