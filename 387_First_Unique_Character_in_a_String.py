class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for x in s:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1
