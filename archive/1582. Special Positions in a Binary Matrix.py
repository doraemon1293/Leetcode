from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=[sum(row) for i,row in enumerate(mat)]
        col=[sum(col) for j,col in enumerate(zip(*mat))]
        print(row,col)
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==row[i]==col[j]==1:
                    ans+=1
        return ans