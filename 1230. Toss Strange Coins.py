class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        memo = {}

        def dp(i, target):
            if (i, target) in memo:
                return memo[i, target]
            if target == 0:
                res = 1
                for p in prob[i:]:
                    res *= (1 - p)
                memo[i, target] = res
                return res
            if target == len(prob) - i + 1:
                res = 1
                for p in prob[i:]:
                    res *= p
                memo[i, target] = res
                return res
            if target>len(prob)-i+1:
                return 0
            res=prob[i]*dp(i + 1, target - 1)+(1-prob[i])*dp(i+1,target)
            memo[res,target]=res
            return res
        return dp(0,target)
