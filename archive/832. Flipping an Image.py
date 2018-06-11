class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i]=A[i][::-1]
            A[i]=[0 if x==1 else 1 for x in A[i]]
        return A
A=[[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(A))

