class Solution:
    def minInsertions(self, s: str) -> int:

        stack = []
        ans = 0
        s=s+"("
        for ch in s:
            # print(ch,stack)
            if ch == ")":
                if stack and stack[-1] == ")":
                    if len(stack) >= 2 and stack[-2] == "(":
                        stack.pop()
                        stack.pop()
                    else:
                        ans += 1
                        stack.pop()
                else:
                    stack.append(ch)
            elif ch == "(":
                if len(stack) == 0 or stack[-1] == "(":
                    stack.append(ch)
                else:
                    if len(stack) >= 2 and stack[-2] == "(":
                        ans += 1
                        stack.pop()
                        stack.pop()
                    else:
                        ans += 2
                        stack.pop()
                    stack.append("(")

            # print(ans)
        stack.pop()
        ans+=2*len(stack)
        return ans