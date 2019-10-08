from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        i, j = 0, len(nums1)
        while i <= j:
            splitNums1 = int((i + j) / 2)
            splitNums2 = int((len(nums1) + len(nums2) + 1) / 2 - splitNums1)
            if splitNums1 == 0:
                maxLeftNums1 = float('-inf')
            else:
                maxLeftNums1 = nums1[splitNums1 - 1]
            if splitNums2 == 0:
                maxLeftNums2 = float('-inf')
            else:
                maxLeftNums2 = nums2[splitNums2 - 1]
            if splitNums1 == len(nums1):
                minRightNums1 = float('inf')
            else:
                minRightNums1 = nums1[splitNums1]
            if splitNums2 == len(nums2):
                minRightNums2 = float('inf')
            else:
                minRightNums2 = nums2[splitNums2]
            if maxLeftNums1 <= minRightNums2 and minRightNums1 >= maxLeftNums2:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2.0
                else:
                    return max(maxLeftNums1, maxLeftNums2)
            elif maxLeftNums1 > minRightNums2:
                j = splitNums1 - 1
            else:
                i = splitNums1 + 1
        return 0.0