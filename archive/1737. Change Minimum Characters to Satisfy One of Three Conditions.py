import collections
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a=collections.Counter(a)
        b=collections.Counter(b)
        ans=sum(a.values())-max(a.values())+sum(b.values())-max(b.values())
        for delta in range(26):
            pilot=chr(ord("a")+delta)
            #1
            #all(a)<pilot all(b) >=pilot
            if pilot!="a":
                count=0
                for k in a:
                    if k>=pilot:
                        count+=a[k]
                for k in b:
                    if k<pilot:
                        count+=b[k]
                ans=min(ans,count)
            #2
            # all(b)<pilot all(a) >=pilot
            if pilot!="a":
                count=0
                for k in b:
                    if k>=pilot:
                        count+=b[k]
                for k in a:
                    if k<pilot:
                        count+=a[k]
                ans=min(ans,count)
        return ans


