class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        MOD=10**9+7
        for i in range(1,n+1):
            b=bin(i)[2:]
            ans=(ans<<len(b))%MOD
            ans=(ans+i)%MOD
        return ans
