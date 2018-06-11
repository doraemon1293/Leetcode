class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        #f(x)=probbility of x
        #dp(x)=sum(f(y)) 0<=y<=x
        #cuz f(x)=1/W*(sum(f(x-i))=1/W*(dp(x-1)-dp(x-W-1)) 1<=i<=W
        #so dp(x)=dp(x-1)+f(x)=dp(x-1)+1/W*(dp(x-1)-dp(x-W-1))
        if K == 0: return 1
        up_bound=min(K+W-1,N)
        dp=[0]*(up_bound+1)
        dp[0]=1.0
        for x in range(1,up_bound+1):
            if x>K:
                dp[x]=dp[x-1]+(dp[K-1]-(dp[x-W-1] if x-W-1>=0 else 0))/W
            else:
                dp[x]=dp[x-1]+(dp[x-1]-(dp[x-W-1] if x-W-1>=0 else 0))/W

        return dp[N]-dp[K-1]
N = 21
K = 17
W = 10
print(Solution().new21Game(N,K,W))
