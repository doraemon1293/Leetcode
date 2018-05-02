class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        import bisect
        arr = sorted([(num, ind) for ind, num in enumerate(difficulty)])
        pro = 0
        d = {}
        for num, ind in arr:
            pro = max(profit[ind], pro)
            d[num] = pro
        ans = 0
        arr = [x[0] for x in arr]
        # print(arr)
        # print(d)
        for diff in worker:
            ind = bisect.bisect_right(arr, diff)
            if ind != 0:
                ans += d[arr[bisect.bisect_right(arr, diff) - 1]]
        return ans


difficulty = [2, 4, 4, 4, 6, 8, 10]
profit = [10, 20, 15, 25, 30, 40, 50]
worker = [4, 5, 6, 7]

difficulty = [85, 47, 57]
profit = [24, 66, 99]
worker = [40, 25, 25]
print(Solution().maxProfitAssignment(difficulty, profit, worker))
