class Solution:
    def isHappy(self, n: int) -> bool:
        num_seen = set()

        while n != 1:
            if n in num_seen:
                return False

            num_seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))

        return True