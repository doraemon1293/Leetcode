import itertools
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets=itertools.chain.from_iterable(itertools.combinations(nums,l) for l in range(len(nums) + 1))
        def foo(arr):
            res=0
            for x in arr:
                res^=x
            return res
        return sum(foo(arr) for arr in subsets)