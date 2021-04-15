from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M,N=len(matrix),len(matrix[0])
        arrs=[[0]*N for _ in range(M)]
        temp=[]
        for i in range(M):
            for j in range(N):
                if i==0 and j==0:
                    arrs[i][j]=matrix[i][j]
                elif i==0:
                    arrs[i][j]=arrs[i][j-1]^matrix[i][j]
                elif j==0:
                    arrs[i][j]=arrs[i-1][j]^matrix[i][j]
                else:
                    arrs[i][j]=arrs[i-1][j-1]^arrs[i][j-1]^arrs[i-1][j]^matrix[i][j]
                temp.append(arrs[i][j])
        # for arr in arrs:
        #     print(arr)
        temp.sort(reverse=True)
        return temp[k-1]



print(Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 1))
