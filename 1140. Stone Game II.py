class Solution:
    def stoneGameII(self, piles: list) -> int:
        sum_remain = [0]
        for i in range(len(piles) - 1, -1, -1):
            sum_remain.append(sum_remain[-1] + piles[i])

        memo={}
        def dp(remain, M):
            if 2 * M >= remain:
                return sum_remain[remain]
            if (remain,M) in memo:
                return memo[remain,M]
            mini = float("inf")
            for x in range(1, 2 * M+1):
                temp = dp(remain - x, max(x, M))
                mini = min(mini, temp)
            memo[remain,M]=sum_remain[remain] - mini
            return sum_remain[remain] - mini

        return dp(len(piles), 1)


piles = [2, 7, 9, 4, 4]
piles=[8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]
print(Solution().stoneGameII(piles))
