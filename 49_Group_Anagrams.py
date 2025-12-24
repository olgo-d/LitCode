from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dct = defaultdict(list)

        for x in strs:
            word = ''.join(sorted(x))
            anagrams_dct[word].append(x)

        return list(anagrams_dct.values())