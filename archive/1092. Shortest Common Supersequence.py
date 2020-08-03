class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[""] * (len(str2) + 1) for i in range(len(str1) + 1)]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                        dp[i + 1][j + 1] = dp[i + 1][j]
                    else:
                        dp[i + 1][j + 1] = dp[i][j + 1]
        lcs = dp[-1][-1]
        i = j = 0
        ans = ""
        for ch in lcs:
            while str1[i] != ch:
                ans += str1[i]
                i += 1
            while str2[j] != ch:
                ans += str2[j]
                j += 1
            i += 1
            j += 1
            ans += ch
        ans+=str1[i:]
        ans+=str2[j:]
        return ans


str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2))
