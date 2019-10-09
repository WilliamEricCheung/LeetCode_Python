from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()
        if len(matrix) == 0:
            return ans
        top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if top < bottom and left < right:
                for i in range(right - 1, left, -1):
                    ans.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    ans.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans