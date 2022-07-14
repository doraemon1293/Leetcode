class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        pre_sum = 0
        summ = sum(nums)
        ans = -float("inf")
        for i, num in enumerate(nums):
            front = pre_sum + num
            back = summ - pre_sum
            ans = max(ans, front, back)
        return ans
