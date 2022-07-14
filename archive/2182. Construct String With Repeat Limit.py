import collections

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        c = collections.Counter(s)
        stack = []
        for k, v in c.items():
            stack.append([k, v])
        stack.sort()
        while stack:
            if ans==[] or ans[-1]!=stack[-1][0]:
                ans += [stack[-1][0]] * min(stack[-1][1], repeatLimit)
                stack[-1][1] -= min(stack[-1][1], repeatLimit)
                if stack[-1][1]==0:
                    stack.pop()
            else:
                if len(stack)<=1:
                    break
                else:
                    ans.append(stack[-2][0])
                    stack[-2][1]-=1
                    if stack[-2][1]==0:
                        temp=stack.pop()
                        stack.pop()
                        stack.append(temp)
        return "".join(ans)

