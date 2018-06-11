class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans=0
        st=0
        N=len(A)
        while st<len(A):
            mid=st
            while mid<len(A)-1 and A[mid]<A[mid+1]:
                mid+=1
            end=mid
            while end<len(A)-1 and A[end]>A[end+1]:
                end+=1
            if st<mid<end and end-st+1>=3 and end-st+1>ans:
                ans=end-st+1
            if end==N-1 or A[end]>=A[end+1]:
                st=end+1
            else:
                st=end
        return ans

A=[2, 1, 4, 7, 3, 2, 5]
A=[2,2,2]
A=[1,2,1]
A=[0,1,2,3,4,5,6,7,8,9]
print(Solution().longestMountain(A))
