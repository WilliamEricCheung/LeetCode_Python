from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        length = len(height)
        leftMax = [0] * length
        rightMax = [0] * length
        leftMax[0] = height[0]
        rightMax[length - 1] = height[length - 1]
        for i in range(1, length):
            leftMax[i] = max(height[i], leftMax[i-1])
        for i in range(length - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        ans = 0
        for i in range(0, length):
            ans += min(leftMax[i], rightMax[i]) - height[i]
        return ans