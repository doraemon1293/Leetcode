class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1, s1 = 0, 1
        for i in range(1, len(A)):
            n2=s2=float("inf")
            if A[i-1]<A[i] and B[i-1]<B[i]:
                n2=min(n2,n1)
                s2=min(s2,s1+1)
            if A[i-1]<B[i] and B[i-1]<A[i]:
                n2=min(n2,s1)
                s2=min(s2,n1+1)
            n1,s1=n2,s2
        return min(n1,s1)
A=[1,3,5,4]
B=[1,2,3,7]
print(Solution().minSwap(A,B))