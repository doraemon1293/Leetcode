class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1=0
        while p1<len(A) and A[p1] % 2 == 0:
            p1+=1
        p2=p1
        while p2<len(A):
            while p2<len(A) and A[p2]%2==1:
                p2+=1
            if p2<len(A):
                A[p1],A[p2]=A[p2],A[p1]
                p1+=1
                p2+=1
        return A

A=[0]
print(Solution().sortArrayByParity(A))