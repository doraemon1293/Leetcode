import math
from typing import List
from collections import Counter


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD=10**9+7
        maxi = max(nums)
        c = Counter(nums)
        pre_freq = [0]
        for x in range(1, maxi + 1):
            pre_freq.append(pre_freq[-1] + c.get(x, 0))

        def numbers_between_low_high(low, high):
            if high >= len(pre_freq):
                high = len(pre_freq) - 1
            if low >= len(pre_freq):
                low = len(pre_freq) - 1
            return pre_freq[high] - pre_freq[low - 1]

        # print(pre_freq)
        ans = 0
        for i in range(1, maxi + 1):
            if i in c:

                for multi in range(1, math.floor(maxi / i)+1):
                    low, high = multi * i, (multi + 1) * i - 1
                    count = numbers_between_low_high(low, high)
                    ans =(ans+ count * multi * c[i])%MOD
                    # print(multi,low, high, count, ans,math.floor(maxi / i)+1)
        return ans