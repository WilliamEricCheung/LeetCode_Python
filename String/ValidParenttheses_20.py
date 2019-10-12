class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) % 2 != 0:
            return False
        for ch in s:
            if dict.get(ch) is not None:
                stack.append(ch)
            elif ch in dict.values():
                if len(stack) == 0 or dict[stack.pop()] != ch:
                    return False
        return len(stack) == 0