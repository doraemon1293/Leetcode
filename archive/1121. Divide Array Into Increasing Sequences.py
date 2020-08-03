import collections
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        counter=collections.Counter(nums)
        return max(counter.values())*K<=len(nums)
