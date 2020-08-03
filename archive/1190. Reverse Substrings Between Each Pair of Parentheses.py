class Solution:
    def reverseParentheses(self, s: str) -> str:
        s=list(s)
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                st=stack.pop()
                end=i
                s[st+1:end]=s[st+1:end][::-1]
        return "".join([ch for ch in s if ch not in ("(",")")])
