from typing import List


class Solution:
    """贪心算法在这里是不正确的，需要使用动态规划"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        return -1 if dp[amount] > amount else dp[amount]
