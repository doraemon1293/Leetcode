from typing import List
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        L=len(nums)
        print(L)
        if k==0:
            return nums[0]
        if L==1:
            if k%2==0:
                return nums[0]
            if k%2:
                return -1
        if k<=L+1:
            if k+1<=L:
                return max(nums[:k - 1]+[nums[k]])
            else:
                return max(nums[:k-1])
        if k>L+1:
            return max(nums)
nums=[35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49]
k=15
print(Solution().maximumTop(nums,k))