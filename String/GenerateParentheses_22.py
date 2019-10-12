from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backTrack(ans, "", 0, 0, n)
        return ans

    def backTrack(self, ans: List[str], cur: str, open: int, close: int, limit: int):
        if len(cur) == limit * 2:
            ans.append(cur)
            return
        if open < limit:
            self.backTrack(ans, cur + '(', open + 1, close, limit)
        if close < open:
            self.backTrack(ans, cur + ')', open, close + 1, limit)