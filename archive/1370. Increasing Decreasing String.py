import collections
class Solution:
    def sortString(self, s: str) -> str:
        c=collections.Counter(s)
        keys=sorted(c.keys())
        r_keys=keys[::-1]
        ans=[]
        while len(ans)<len(s):
            for ch in keys:
                if c[ch]:
                    ans.append(ch)
                    c[ch]-=1
            for ch in r_keys:
                if c[ch]:
                    ans.append(ch)
                    c[ch]-=1
        return "".join(ans)


