class Solution:
    def maxDepth(self, s: str) -> int:
        s=[ch  for ch in s if ch in ("(",")")]
        stack=[]
        ans=0
        for ch in s:
            if ch=="(":
                stack.append(ch)
                ans=max(ans,len(stack))
            else:
                stack.pop()
        return ans


