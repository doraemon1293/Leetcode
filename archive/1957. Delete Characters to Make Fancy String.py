class Solution:
    def makeFancyString(self, s: str) -> str:
        last=None
        length=0
        ans=[]
        s+=" "
        for ch in s:
            if ch==last:
                length+=1
                if length<3:
                    ans.append(ch)
            else:
                ans.append(ch)
                last=ch
                length=1
        return "".join(ans[:-1])

