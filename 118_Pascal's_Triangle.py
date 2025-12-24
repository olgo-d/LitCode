from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[]] * numRows

        for i in range(numRows):
            triangle[i] = [1] * (i + 1)

            for j in range(1, i//2+1):
                triangle[i][i-j] = triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle