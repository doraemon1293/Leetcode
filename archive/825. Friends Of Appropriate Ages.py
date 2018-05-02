class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        import bisect
        ages.sort()
        ans=0
        for i,A in enumerate(ages):
            if A<=100:
                st=bisect.bisect_right(ages,A/2+7)
                end=bisect.bisect_right(ages,A)
                ans+=0 if st>=end else end-st-1
            else:
                st=bisect.bisect_right(ages,A/2+7)
                end=bisect.bisect_right(ages,A)
                ans+=0 if st>=end else end-st-1
        return ans
ages=[20,30,100,110,120]
#ages=[16,17,18]
#ages=[16,16]

print(Solution().numFriendRequests(ages))

