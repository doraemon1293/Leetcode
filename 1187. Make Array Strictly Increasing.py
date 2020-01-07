import bisect
import collections


class Solution:
    def makeArrayIncreasing(self, arr1: list, arr2: list) -> int:
        dp = {-1: 0}
        arr2 = sorted(set(arr2))
        for a1 in arr1:
            new_dp = collections.defaultdict(lambda: float("inf"))

            for k in dp:
                if a1 > k:
                    new_dp[a1] = min(new_dp[a1], dp[k])
                ind = bisect.bisect_right(arr2, k)
                if ind < len(arr2):
                    new_dp[arr2[ind]] = min(new_dp[arr2[ind]], dp[k]+1)
            dp=new_dp
            # print(dp)
        return min(dp.values()) if dp else -1


arr1 = [0, 11, 6, 1, 4, 3]
arr2 = [5, 4, 11, 10, 1, 0]
print(Solution().makeArrayIncreasing(arr1, arr2))
