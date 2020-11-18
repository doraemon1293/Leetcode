import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            ind=bisect.bisect_left(nums,i)
            if len(nums)-ind==i:
                return i
        return -1