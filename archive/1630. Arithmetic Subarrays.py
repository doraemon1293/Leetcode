from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def foo(arr):
            if len(arr)<=2:
                return True
            delta=arr[0]-arr[1]
            for i in range(len(arr)-1):
                if arr[i]-arr[i+1]!=delta:
                    return False
            return True

        ans=[]
        for left,right in zip(l,r):
            arr=nums[left:right+1]
            arr.sort()
            ans.append(foo(arr))
        return ans


