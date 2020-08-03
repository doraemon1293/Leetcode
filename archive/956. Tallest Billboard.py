class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        memo = {}

        def dp(i, diff):
            if (i, diff) in memo:
                return memo[i, diff]

            if i == len(rods):
                if diff==0:
                    return 0
                else:
                    return float("-inf")
            memo[i, diff] = max(dp(i + 1, diff), dp(i + 1, diff-rods[i]),dp(i+1,diff+rods[i])+rods[i])
            return memo[i, diff]

        return dp(0, 0)


rods = [1, 2, 3, 4, 5, 6, 7]
print(Solution().tallestBillboard(rods))
