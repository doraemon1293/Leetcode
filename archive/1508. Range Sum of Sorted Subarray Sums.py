from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_array = []

        for i in range(len(nums)):
            temp = nums[i]
            new_array.append(temp)
            for j in range(i + 1, len(nums)):
                temp += nums[j]
                new_array.append(temp)
        new_array.sort()

        ans=0
        MOD=10**9+7
        for i in range(left-1,right):
            ans+=new_array[i]
            ans%=MOD
        return ans