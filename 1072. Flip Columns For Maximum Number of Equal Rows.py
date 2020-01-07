class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        d={}
        ans=0
        for row in matrix:
            row=tuple(row)
            d.setdefault(row,0)
            d[row]+=1
        for k in d:
            k1=k
            k2=tuple([0 if x else 1 for x in k1])
            ans=max(ans,d.get(k1,0)+d.get(k2,0))
        return ans


matrix=[[0,1],[1,0]]
print(Solution().maxEqualRowsAfterFlips(matrix))