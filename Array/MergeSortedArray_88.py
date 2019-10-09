from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m + n - 1, -1, -1):
            mm = nums1[m - 1] if m - 1 >= 0 else -2 ** 32
            nn = nums2[n - 1] if n - 1 >= 0 else -2 ** 32
            nums1[i] = max(mm, nn)
            if mm < nn:
                n -= 1
            else:
                m -= 1
