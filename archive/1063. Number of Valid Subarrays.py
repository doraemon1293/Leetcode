class Solution:
    def validSubarrays(self, nums: list) -> int:
        stack = []
        ans = 0
        N = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][0] >= nums[i]:
                stack.pop()
            ans += stack[-1][1] - i if stack else N - i
            stack.append([nums[i],i])
        return ans


nums=[1,4,2,5,3]
print(Solution().validSubarrays(nums))