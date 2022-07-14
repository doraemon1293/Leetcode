import bisect
from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        idxs = [i for i in range(len(nums)) if nums[i] % p == 0]
        # ans=0
        sub_arr = set()
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                left_ind = bisect.bisect_left(idxs, left)
                right_ind = bisect.bisect_right(idxs, right)
                if right_ind - left_ind <= k:
                    t = tuple(nums[left:right + 1])
                    sub_arr.add(t)
        return len(sub_arr)