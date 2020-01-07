class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo,hi=len(nums),10**6
        def foo(div,nums):
            nums=[num//div+bool(nums%div) for num in nums]
            return sum(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if foo(div,nums)>threshold:
                lo=mid+1
            else:
                hi=mid
        return lo


