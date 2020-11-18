import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        c=collections.Counter(s)
        used=set()
        ans=0
        for freq,ch in sorted([(v,k) for k,v in c.items()]):
            if freq not in used:
                used.add(freq)
            else:
                temp=freq
                while temp>0 and temp in used:
                    temp-=1
                ans+=freq-temp
                used.add(temp)
        return ans


