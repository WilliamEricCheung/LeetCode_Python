from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[0] * (n + 1)] * (m + 1)
        length = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    print(i, j, dp[i][j])
                    length = max(length, dp[i][j])
        return length * length


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
solution = Solution()
ans = solution.maximalSquare(matrix)
print("\n", ans)