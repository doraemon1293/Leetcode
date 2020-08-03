class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        incre = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        ans = 0
        dp = {}
        for i in range(len(s)):
            new_dp = {}
            new_dp[incre.get(s[i], 0)] = 1
            for k, v in dp.items():
                new_dp[k ^ incre.get(s[i], 0)] = max(new_dp.get(k ^ incre.get(s[i], 0), 0), v + 1)
            dp = new_dp
            ans = max(ans, dp.get(0, 0))
        return ans


s = "eleetminicoworoep"
print(Solution().findTheLongestSubstring(s))
