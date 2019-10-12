class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        idx = 0
        ans = 0
        for i in range(0, len(s)):
            if dict.get(s[i]) is not None:
                idx = max(dict.get(s[i]), idx)
            ans = max(ans, i - idx + 1)
            dict[s[i]] = i + 1
        return ans
