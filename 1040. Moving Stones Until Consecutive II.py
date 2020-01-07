import bisect


class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        N = len(stones)
        maxi = max((stones[-2] - stones[0] + 1) - (N - 1), (stones[-1] - stones[1] + 1) - (N - 1))
        mini=float("inf")
        i=0
        for j in range(N):
            while stones[j] - stones[i] >= N:
                i += 1
            if j - i + 1 == N - 1 and stones[j] - stones[i] == N - 2:
                mini = min(mini, 2)
            else:
                mini = min(mini, N - (j - i + 1))


        return [mini, maxi]

stones=[-100,3,4,5,6]
stones=[2,5,6,7,8]
print(Solution().numMovesStonesII(stones))