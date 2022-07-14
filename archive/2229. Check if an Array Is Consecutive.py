class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums=sorted(set(nums))
        return nums==list(range(nums[0],nums[-1]+1)