from typing import List
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        M,N =len(grid),len(grid[0])
        visited=set()
        def dfs(x,y):
            visited.add((x,y))
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                x1,y1=x+dx,y+dy
                if 0<=x1<M and 0<=y1<N and grid[x1][y1] and (x1,y1) not in visited:
                    dfs(x1,y1)
        total=0

        for x in range(M):
            for y in range(N):
                if grid[x][y]:
                    total+=1
        for x in range(M):
            for y in range(N):
                if grid[x][y]:
                    dfs(x,y)
                    if len(visited)<total:
                        return 0
                    break


        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    visited=set()
                    grid[i][j]=0
                    for x in range(M):
                        for y in range(N):
                            if grid[x][y]:
                                dfs(x,y)
                                if len(visited)<total-1:
                                    return 1
                    grid[i][j]=1
        return 2