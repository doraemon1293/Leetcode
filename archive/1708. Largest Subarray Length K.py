from typing import List
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        largest_ind=None

        for i in range(len(nums)-k+1):
            if largest_ind==None or nums[largest_ind]<nums[i]:
                largest_ind=i
        return nums[largest_ind:largest_ind+k]

