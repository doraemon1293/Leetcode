import collections
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        M,N=len(grid),len(grid[0])
        dis=[[-1]*N for _ in range(M)]
        ans=-1
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    dis[i][j]=0
                    q.append((i,j))
        while q:
            i,j=q.popleft()
            for x,y in ((i-1,j),(i,j-1),(i+1,j),(i,j+)):
                if 0<=x<M and 0<=y<N:
                    if dis[x][y]==-1:
                        dis[x][y]=1+dis[i][j]
                        q.append((x,y))
                        ans=max(ans,dis[x][y])
        return ans

