class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        candies.sort()
        lo=1
        hi=candies[-1]
        ans=0
        while lo<=hi:
            mid=(lo+hi)//2
            temp=sum([x//mid for x in candies])
            if temp>=k:
                ans=max(ans,mid)
                lo=mid+1
            else:
                hi=mid-1
            # print(lo,hi)
        return ans