class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        N = len(regular)
        dp = [0, expressCost]  # [i,0] ith stop in regular line [i,1] ith stop in express line
        ans = []
        for i in range(1, N + 1):
            r_r = dp[0] + regular[i - 1]  # from regular to regular
            r_e = dp[0] + expressCost + express[i - 1]  # from regular to express
            e_r = dp[1] + regular[i - 1]  # from express to regular
            e_e = dp[1] + express[i - 1]  # from express to express
            new_dp = [min(e_r, r_r), min(r_e, e_e)]
            ans.append(min(new_dp))
            dp = new_dp
        return ans


