class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(amount + 1):
                if j+coin<=amount:
                    dp[j+coin] += dp[j]
        return dp[amount]


amount = 500
coins = [3, 5, 7, 8, 9, 10, 11]
amount = 1000
coins = [3, 5, 7, 8, 9, 10, 11]
print(Solution().change(amount, coins))
