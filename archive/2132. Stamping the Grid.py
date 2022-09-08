class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        M,N=len(grid),len(grid[0])
        pre_sum=[[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                pre_sum[i+1][j+1]=pre_sum[i][j+1]+pre_sum[i+1][j]-pre_sum[i][j]+grid[i][j]

        def summ(x1,y1,x2,y2):
            return pre_sum[x2+1][y2+1]-pre_sum[x1][y2+1]-pre_sum[x2+1][y1]+pre_sum[x1][y1]

        diff=[[0]*(N+1) for _ in range(M+1)]
        for x in range(M-stampHeight+1):
            for y in range(N-stampWidth+1):
                if summ(x,y,x+stampHeight-1,y+stampWidth-1)==0:
                    diff[x][y]+=1
                    diff[x+stampHeight][y]-=1
                    diff[x][y+stampWidth]-=1
                    diff[x+stampHeight][y+stampWidth]+=1

        pre_sum2=[[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                pre_sum2[i+1][j+1]=pre_sum2[i][j+1]+pre_sum2[i+1][j]-pre_sum2[i][j]+diff[i][j]

        for x in range(M):
            for y in range(N):
                if pre_sum2[x+1][y+1]<=0:
                    if grid[x][y]==0:
                        return False
        return True