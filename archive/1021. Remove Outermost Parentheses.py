class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans=[]
        temp_str=[]
        stack=[]
        for ch in S:
            if ch=="(":
                stack.append(ch)
                temp_str.append(ch)
            else:
                stack.pop()
                temp_str.append(ch)
                if stack==[]:
                    ans.append("".join(temp_str[1:-1]))
                    temp_str=[]
        return "".join(ans)
S="(()())(())"
print(Solution().removeOuterParentheses(S))