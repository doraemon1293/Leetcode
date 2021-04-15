from typing import List
from itertools import combinations
from functools import lru_cache
# for x in itertools.combinations((1,2,3),2):
#     print(x)

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums) // k  # the length of each partition
        nums.sort()
        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            res = float("inf")
            for a in combinations(set(nums), d):  # choose a as a partition
                left = list(nums)  # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                res = min(res, max(a) - min(a) + helper(tuple(left)))
            return res

        ans = helper(tuple(nums))  # turn the input into a tuple so the function can be cached
        return ans if ans !=float("inf") else -1
