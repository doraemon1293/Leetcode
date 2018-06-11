class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        N=len(A)
        s=set()
        d=defaultdict(int)
        for i in range(N):
            for j in range(N):
                if B[i][j]:
                    s.add((i,j))
        for i in range(N):
            for j in range(N):
                if A[i][j]:
                    for x,y in s:
                        d[x-i,y-j]+=1
        #print(d)
        ans=max(d.values()) if d else 0
        return ans

A=[[1,1,0],[0,1,0],[0,1,0]]
B=[[0,0,0],[0,1,1],[0,0,1]]
A=[]
B=[]
A=[[0,1],[1,1]]
B=[[1,1],[1,0]]
print(Solution().largestOverlap(A,B))

