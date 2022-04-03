class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        return sum(1 for i in range(len(nums)) for j in range(nums) if abs(nums[i]-nums[j])==k and i!=j)