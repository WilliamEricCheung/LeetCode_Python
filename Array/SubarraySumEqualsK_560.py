from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = {0:1}
        cnt, sum = 0,0
        for num in nums:
            sum += num
            if dict.__contains__(sum - k):
                cnt+=dict.get(sum - k)
            dict[sum] = (0 if (dict.get(sum) == None) else dict.get(sum)) + 1
        return cnt