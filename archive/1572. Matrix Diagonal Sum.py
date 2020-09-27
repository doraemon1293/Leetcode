class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N=len(mat)
        s=set()
        for i in range(N):
            s.add((i,i))
            s.add((i,N-1-i))
        return sum(mat[i][j] for i,j in s)

