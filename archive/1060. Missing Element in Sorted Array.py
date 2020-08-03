class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        p = 1
        while p < len(nums) and k:
            temp = nums[p] - nums[p - 1] - 1
            if temp >= k:
                return nums[p - 1] + k
            else:
                k -= temp
                p += 1
        return nums[-1] + k
