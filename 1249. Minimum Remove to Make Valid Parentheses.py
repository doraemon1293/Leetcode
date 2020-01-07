class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        to_delete=[]
        for i,ch in enumerate(s):
            if ch=="(":
                stack.append((ch,i))
            if ch==")":
                if stack:
                    stack.pop()
                else:
                    to_delete.append(i)
        to_delete+=[x[1] for x in stack]
        s=list(s)
        for i in to_delete:
            s[i]=""
        return "".join(s)

