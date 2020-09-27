from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        dp = {0: 0}
        size1 = len(cost)
        size2 = len(cost[0])
        min_cost_to_connect_point_in_group2 = [min([cost[i][j] for i in range(size1)]) for j in range(size2)]
        for i in range(size1):
            new_dp = {}
            for state in dp:
                cost_ = dp[state]
                for j in range(size2):
                    new_state = state | (1 << j)
                    new_cost = cost_ + cost[i][j]
                    if new_state in new_dp:
                        new_dp[new_state] = min(new_dp[new_state], new_cost)
                    else:
                        new_dp[new_state] = new_cost
            dp = new_dp
        ans = float("inf")
        for state in dp:
            cost_ = dp[state]
            for j in range(size2):
                if (state >> j) & 1 == 0:
                    cost_ += min_cost_to_connect_point_in_group2[j]
            ans = min(ans, cost_)
        return ans


cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
cost = [[58, 83, 15, 13, 68, 58, 66, 100, 40, 97, 46, 80], [91, 74, 64, 39, 9, 34, 37, 35, 45, 45, 37, 27],
        [5, 70, 44, 0, 37, 59, 21, 50, 26, 64, 62, 44], [46, 72, 14, 65, 87, 82, 53, 45, 64, 22, 93, 36],
        [8, 8, 25, 9, 78, 52, 4, 75, 69, 29, 4, 38], [42, 77, 37, 75, 57, 39, 85, 89, 64, 8, 100, 52],
        [5, 83, 55, 13, 19, 82, 92, 83, 9, 99, 16, 34], [21, 79, 91, 76, 99, 83, 59, 67, 85, 0, 21, 60],
        [94, 6, 80, 60, 85, 4, 38, 8, 83, 100, 11, 76], [100, 70, 18, 33, 59, 53, 99, 97, 20, 49, 65, 94],
        [94, 42, 99, 8, 87, 15, 42, 46, 11, 51, 96, 91], [10, 9, 90, 81, 75, 90, 25, 56, 84, 39, 96, 49]]
print(Solution().connectTwoGroups(cost))
