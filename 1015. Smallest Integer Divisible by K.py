class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K==1: return 1
        ans=1
        mod=1
        s=set(1)
        while mod:
            ans+=1
            mod=(mod*10+1)%K
            if mod in s:
                return -1
        return ans

