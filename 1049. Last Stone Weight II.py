class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        summs = {0}
        for stone in stones:
            summs = set([summ + stone for summ in summs] + [summ - stone for summ in summs])
        return min([abs(x) for x in summs])


stones = [1, 1, 4, 2, 2]
print(Solution().lastStoneWeightII(stones))
