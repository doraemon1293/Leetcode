class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x=str(x)
        if n[0]!="-":
            for i in range(len(n)):
                if x>n[i]:
                    return n[:i]+x+n[i:]
            return n+x
        else:
            n=n[1:]
            for i in range(len(n)):
                if x<n[i]:
                    return "-"+n[:i]+x+n[i:]
            return "-"+n+x