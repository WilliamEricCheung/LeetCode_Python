from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultSet = set()
        nums.sort()
        length = len(nums)
        if length < 3:
            return list(resultSet)
        for i in range(2, length):
            if i < length - 1 and nums[i] == nums[i+1]:
                continue
            left, right = 0, i - 1
            while left < right:
                while left < right and nums[left] + nums[right] > - nums[i]:
                    right -= 1
                while left < right and nums[left] + nums[right] < - nums[i]:
                    left += 1
                if left < right and nums[left] + nums[right] + nums[i] == 0:
                    resultSet.add((nums[left], nums[right], nums[i]))
                    leftValue, rightValue = nums[left], nums[right]
                    while left < right and leftValue == nums[left]:
                        left += 1
                    while left < right and rightValue == nums[right]:
                        right -= 1
        return list(resultSet)

