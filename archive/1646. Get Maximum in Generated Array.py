class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                nums[i] = 0
            elif i == 1:
                nums[i] = 1
            elif i % 2 == 0:
                nums[i] = nums[i // 2]
            elif i % 2 == 1:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
        return max(nums)

