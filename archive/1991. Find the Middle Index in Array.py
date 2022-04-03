class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        summ=sum(nums)
        left=0
        for i,n in enumerate(nums):
            right=summ-left-n
            if left==right:
                return i
            left+=n
        return -1