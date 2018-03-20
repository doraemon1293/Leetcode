# coding=utf-8
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def divide(A,R):
            res=[]
            st=0
            while st<len(A):
                while st<len(A) and A[st]>R:
                    st+=1
                if st<len(A):
                    end=st
                    while end<len(A) and A[end]<=R:
                        end+=1
                    res.append(A[st:end])
                    st=end
            return  res
        arrs=divide(A,R)
        print(arrs)
        ans=0
        for arr in arrs:
            count = 0
            for i in range(len(arr)):
                count+=1
                if arr[i]>=L:
                    ans+=count*(len(arr)-i)
                    count=0
        return  ans

A=[2,1,4,3]
L=2
R=3
print(Solution().numSubarrayBoundedMax(A,L,R))