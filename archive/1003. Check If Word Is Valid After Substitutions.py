class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for ch in S:
            if ch == "c":
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
