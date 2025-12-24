from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dubl_dct = defaultdict(int)

        for num in nums:
            dubl_dct[num] += 1

        result = sorted(dubl_dct, key=dubl_dct.get, reverse=True)[:k]

        return result