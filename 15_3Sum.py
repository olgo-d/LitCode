from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]

                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result