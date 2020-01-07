class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        memo = {}

        def change(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            left, right = i, j
            res = 0
            while left < right:
                if s[left] != s[right]:
                    res += 1
                left += 1
                right -= 1
            memo[i,j]=res
            return res

        dp=[change(0,i) for i in range(len(s))]
        # print(dp)
        for k in range(2,k+1):
            new_dp=[None]*(k-1)+[0]
            for i in range(k,len(s)):
                mini=float("inf")
                for j in range(k-2,i):
                    mini=min(dp[j]+change(j+1,i),mini)
                new_dp.append(mini)
            dp=new_dp
            # print(k,dp)
        return dp[-1]




s = "leetcode"
k = 7
print(Solution().palindromePartition(s,k))