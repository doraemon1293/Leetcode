class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m,n=len(A),len(A[0])
        for row in range(m):
            if A[row][0]==0:
                A[row]=[1 if x==0 else 0 for x in A[row]]

        for column in range(n):
            n0=n1=0
            for row in range(m):
                if A[row][column]==0:
                    n0+=1
                else:
                    n1+=1
            if n0>n1:
                for row in range(m):
                    A[row][column]=1 if A[row][column]==0 else 0

        ans=0
        for row in A:
            s="".join([str(x) for x in row])
            ans+=int(s,2)
        return ans

A=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(Solution().matrixScore(A))


























