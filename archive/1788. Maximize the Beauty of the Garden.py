class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        presum = [0]
        first_last_ind = {}
        for i, x in enumerate(flowers):
            if x not in first_last_ind:
                first_last_ind[x] = [i, -1]
            else:
                first_last_ind[x][1] = i
            if x > 0:
                presum.append(presum[-1] + x)
            else:
                presum.append(presum[-1])

        def get_sum_x_y(x, y):
            if x > y:
                return 0
            return presum[y + 1] - presum[x]

        ans = -float("inf")
        for k in first_last_ind:
            first, last = first_last_ind[k]
            if last != -1:
                ans = max(ans, 2 * k + get_sum_x_y(first + 1, last - 1))
        return ans