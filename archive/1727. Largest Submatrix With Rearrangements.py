from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M,N=len(matrix),len(matrix[0])
        height=[0]*N
        ans=0
        for x in range(M):
            for y in range(N):
                height[y]=height[y]+1 if matrix[x][y] else 0
            sorted_height=sorted([x for x in height if x!=0])
            for j in range(len(sorted_height)):
                ans=max(ans,sorted_height[j]*(len(sorted_height)-j))
        return ans






