#coding=utf-8
class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m,n=len(grid),len(grid[0])
        def dfs(x,y):
            if 0<=x<m and 0<=y<n and grid[x][y]==1:
                res = 1
                grid[x][y]=2
                for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    res+=dfs(x+dx,y+dy)
                return res
            return 0

        def connected(x,y):
            if x==0:
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]==2:
                    return True
            return False

        for x,y in hits:
            if grid[x][y]==0:
                grid[x][y]=-1
            else:
                grid[x][y]=0
        print(grid)
        for i in range(n):
            dfs(0,i)
        print(grid)
        ans=[]
        for x,y in hits[::-1]:
            if grid[x][y]==-1:
                grid[x][y]=0
                ans.append(0)
            else:
                grid[x][y]=1
                if connected(x,y):
                    ans.append(dfs(x,y)-1)
                else:
                    ans.append(0)
        return ans[::-1]


grid=[[1,0,0,0],[1,1,1,0]]
hits=[[1,0]]
print(Solution().hitBricks(grid,hits))