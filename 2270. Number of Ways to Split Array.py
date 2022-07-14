class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        summ = sum(nums)
        summ_left = 0
        ans = 0
        for i in range(len(nums) - 1):
            summ_left += nums[i]
            summ -= nums[i]
            if summ_left >= summ:
                ans += 1
        return ans

