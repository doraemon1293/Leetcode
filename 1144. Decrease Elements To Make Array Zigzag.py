class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        odd = even = 0
        for i in range(len(nums)):
            temp = max(nums[i] - (nums[i + 1] if i + 1 < len(nums) else float("inf")), nums[i] - (nums[i - 1] if i - 1 >= 0 else float("inf")))
            if temp >= 0:
                if i % 2:
                    odd += temp + 1
                else:
                    even += temp + 1
        return min(odd,even)