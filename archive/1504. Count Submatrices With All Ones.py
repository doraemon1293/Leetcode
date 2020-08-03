from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M,N=len(mat),len(mat[0])
        pre_mat=[]
        for i in range(M):
            temp=[0]*N
            for j in range(N-1,-1,-1):
                if mat[i][j]==1:
                    temp[j]=(temp[j+1] if j+1<=N-1 else 0)+1
            pre_mat.append(temp)
        # print(pre_mat)
        ans=0
        for j in range(N):
            for i in range(M):
                if pre_mat[i][j]:
                    ans+=pre_mat[i][j]
                    mini=pre_mat[i][j]
                    for k in range(i+1,M):
                        mini=min(pre_mat[k][j],mini)
                        if mini:
                            ans+=mini
                        else:
                            break
        return ans