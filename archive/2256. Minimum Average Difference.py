from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        summ = sum(nums)
        presum = 0
        ans = float("inf")
        ind = None
        n = len(nums)
        for i, num in enumerate(nums):
            presum += num
            postsum = summ - presum
            # print(presum,postsum)
            # if n-i-1:
            # print(presum//(i+1),postsum//(n-i-1))
            diff = abs(presum // (i + 1) - (postsum // (n - i - 1) if (n - i - 1) != 0 else 0))
            if ans > diff:
                ind = i
                ans = diff
        return ind