# coding=utf-8
'''
Created on 2017å¹?10æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def solve(st, end):
            if st + 1 == end:
                res = 1 if lower <= prefix[end] - prefix[st] <= upper else 0
                if prefix[end] < prefix[st]:
                    prefix[end], prefix[st] = prefix[st], prefix[end]
                return res
            if st == end:
                return 0
            else:
                mid = (st + end) / 2
                res = solve(st, mid) + solve(mid + 1, end)
                i = j = mid + 1
                for left in prefix[st:mid + 1]:
                    while i <= end and prefix[i] < lower + left: i += 1
                    while j <= end and prefix[j] <= upper + left:j += 1
                    res += j - i
                prefix[st:end + 1] = sorted(prefix[st:end + 1])
                return res

        print prefix
        return solve(0, len(prefix) - 1)


nums = [-2, 5, -1]
lower = -2
upper = 2

print Solution().countRangeSum(nums, lower, upper)

