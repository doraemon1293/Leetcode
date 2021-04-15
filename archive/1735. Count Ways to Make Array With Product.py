import functools

from typing import List
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD=10**9 + 7
        @functools.lru_cache(None)
        def fac(n):
            x=2
            d={}
            while n>1:
                while n%x==0:
                    d.setdefault(x,0)
                    d[x]+=1
                    n//=x
                x+=1
            return d
        @functools.lru_cache(None)
        def comb(n,k):
            if n==k or k==0:
                return 1
            return comb(n-1,k)+comb(n-1,k-1)
        ans=[]
        for n,prod in queries:
            d=fac(prod)
            res=1
            for k,v in d.items():
                res*=comb(v+n-1,n-1)
                res%=MOD
            ans.append(res)
        return ans






print(Solution().waysToFillArray([[2,6],[5,1],[73,660]]))
