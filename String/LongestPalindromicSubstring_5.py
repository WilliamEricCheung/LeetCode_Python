class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or s.__len__() < 1:
            return ""
        start, end = 0, 0
        for i in range(0, s.__len__()):
            len1 = self.findCenterLength(s, i, i)
            len2 = self.findCenterLength(s, i, i + 1)
            len = max(len1, len2)
            if len > (end - start):
                start = i - int((len - 1) / 2)
                end = i + int(len / 2)
        return s[int(start): int(end) + 1]
    def findCenterLength(self, s: str, left: int, right: int) -> int:
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1