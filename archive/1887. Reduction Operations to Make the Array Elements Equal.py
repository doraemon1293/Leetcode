from typing import List
from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        # mini=min(c)
        keys = sorted(c)
        ans = 0
        for i, key in enumerate(keys):
            ans += i * c[key]
        return ans