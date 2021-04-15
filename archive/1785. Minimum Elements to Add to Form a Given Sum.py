from typing import List
import math


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        summ = sum(nums)
        diff = abs(goal - summ)
        return int(math.ceil(diff / limit))
