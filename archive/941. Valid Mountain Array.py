class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)>=3:
            i=0
            while i<len(A)-1 and A[i+1]>A[i]:
                i+=1
            if i==0 or i==len(A)-1:
                return False
            while i<len(A)-1 and A[i+1]<A[i]:
                i+=1
            if i!=len(A)-1:
                return False
            return True
        else:
            return False