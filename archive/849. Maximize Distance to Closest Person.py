class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        st=0
        ans=0
        if seats[0]==0:
            while st<len(seats) and seats[st]==0:
                st+=1
            ans=st
        st=len(seats)-1
        if seats[-1]==0:
            while st>=0 and seats[st]==0:
                st-=1
            ans=max(len(seats)-st-1,ans)
        st=0
        while st<len(seats):
            end=st
            while end<len(seats) and seats[end]==0:
                end+=1
            length=end-st
            ans=max(ans,(length+1)//2)
            st=end+1
        return ans