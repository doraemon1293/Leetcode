from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        inds={}
        for i,x in enumerate(nums1):
            inds.setdefault(x,[None,None])
            inds[x][0]=i
        for i, x in enumerate(nums2):
            inds.setdefault(x, [None, None])
            inds[x][1] = i
        keys=sorted(inds)
        dp={}
        for num in keys:
            ind1,ind2=inds[num]
            if ind1!=None:
                if ind1==0:
                    dp[num]=max(dp.get(num,0),num)
                else:
                    dp[num]=max(dp.get(num,0),dp[nums1[ind1-1]]+num)
            if ind2 != None:
                if ind2 == 0:
                    dp[num] = max(dp.get(num,0),num)
                else:
                    dp[num] = max(dp.get(num,0),dp[nums2[ind2 - 1]] + num)
        # print(dp)
        return max(dp.values())%(10**9+7)

nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]
nums1 = [1,4,5,8,9,11,19]
nums2 = [2,3,4,11,12]
print(Solution().maxSum(nums1,nums2))