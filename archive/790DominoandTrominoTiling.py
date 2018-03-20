class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans=[0]*(N+1)
        ans[0]=1
        ans[1]=1
        for i in range(2,N+1):
            ans[i]=(ans[i-1]+ans[i-2]+2*sum(ans[:i-2]))%(10**9 + 7)
        print(ans)
        return ans[N]
N=10
print(Solution().numTilings(N))