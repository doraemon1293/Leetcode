class Solution:
    def mctFromLeafValues(self, arr: list) -> int:
        memo = {}
        maxi = {}
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(i, len(arr)):
                temp = max(temp,arr[j])
                maxi[i, j] = temp

        def dp(i, j):
            if i == j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            res = float("inf")
            for k in range(i, j):
                res = min(res, dp(i, k) + dp(k + 1, j) + maxi[i, k] * maxi[k + 1, j])
            memo[i, j] = res
            return res
        return dp(0,len(arr)-1)
        # print(memo)

arr=[6,2,4]
print(Solution().mctFromLeafValues(arr))