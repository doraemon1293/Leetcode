from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        j = 0
        summ = 0
        ans = -1
        target = sum(nums) - x
        print(sum(nums),target)
        # if target==0:
        #     return len(nums)
        while i < len(nums):
            while j < len(nums) and summ < target:
                summ += nums[j]
                j += 1
            if summ == target:
                ans = max(ans, j - i)
            summ-=nums[i]
            i+=1
        return -1 if ans==-1 else len(nums) - ans