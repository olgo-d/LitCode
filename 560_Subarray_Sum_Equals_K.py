from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = defaultdict(int)
        dct[0] = 1
        pref = 0
        result = 0

        for num in nums:
            pref += num
            result += dct[pref - k]
            dct[pref] += 1

        return result