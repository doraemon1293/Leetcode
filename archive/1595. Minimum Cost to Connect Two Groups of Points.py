from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        dp = {0: 0}
        size1 = len(cost)
        size2 = len(cost[0])

        def dfs(j_ind, ori_state, state, cost_, new_dp, i, candidate_j):
            if j_ind == len(candidate_j):
                if ori_state != state:
                    new_dp.setdefault(state, float("inf"))
                    new_dp[state] = min(new_dp[state], cost_)
            else:
                j = candidate_j[j_ind]
                dfs(j_ind + 1, ori_state, state | (1 << j), cost_ + cost[i][j], new_dp, i, candidate_j)
                dfs(j_ind + 1, ori_state, state, cost_, new_dp, i, candidate_j)

        for i in range(size1):
            new_dp = {}
            for state in dp:
                cost_ = dp[state]
                # connect poitn i in Group1 to a point in G2 which is already connected
                mini = float("inf")
                candidate_j = []
                for j in range(size2):
                    if (state >> j) & 1 == 1:
                        mini = min(mini, cost[i][j])
                    else:
                        candidate_j.append(j)
                if mini != float("inf"):
                    new_dp.setdefault(state, float("inf"))
                    new_dp[state] = min(new_dp[state], cost_ + mini)
                # connect point i in Group1 to some points from G2 which is already connected
                dfs(0, state, state, cost_, new_dp, i, candidate_j)
            dp = new_dp
            # print(i, dp)

        return dp[2 ** size2 - 1]


cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
cost = [[58, 83, 15, 13, 68, 58, 66, 100, 40, 97, 46, 80], [91, 74, 64, 39, 9, 34, 37, 35, 45, 45, 37, 27],
        [5, 70, 44, 0, 37, 59, 21, 50, 26, 64, 62, 44], [46, 72, 14, 65, 87, 82, 53, 45, 64, 22, 93, 36],
        [8, 8, 25, 9, 78, 52, 4, 75, 69, 29, 4, 38], [42, 77, 37, 75, 57, 39, 85, 89, 64, 8, 100, 52],
        [5, 83, 55, 13, 19, 82, 92, 83, 9, 99, 16, 34], [21, 79, 91, 76, 99, 83, 59, 67, 85, 0, 21, 60],
        [94, 6, 80, 60, 85, 4, 38, 8, 83, 100, 11, 76], [100, 70, 18, 33, 59, 53, 99, 97, 20, 49, 65, 94],
        [94, 42, 99, 8, 87, 15, 42, 46, 11, 51, 96, 91], [10, 9, 90, 81, 75, 90, 25, 56, 84, 39, 96, 49]]
print(Solution().connectTwoGroups(cost))
