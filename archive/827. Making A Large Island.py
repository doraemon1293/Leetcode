class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        M=len(grid)
        N=len(grid[0])
        visited=set()
        islands=[[-1]*M for _ in range(N)]
        sizes=[]

        def bfs(x,y,island):
            visited.add((x,y))
            islands[x][y]=island
            size=1
            q=deque()
            q.append((x,y))
            while q:
                x0,y0=q.popleft()
                for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                    x1,y1=x0+dx,y0+dy
                    if 0<=x1<M and 0<=y1<N and (x1,y1) not in visited and grid[x1][y1]==1:
                        islands[x1][y1] = island
                        visited.add((x1,y1))
                        q.append((x1,y1))
                        size+=1
            sizes.append(size)

        island=0
        for x in range(M):
            for y in range(N):
                if grid[x][y]==1 and ((x,y) not in visited):
                    bfs(x,y,island)
                    island+=1
        if island==0:
            return 1
        if island==1 and sizes[0]==M*N:
            return sizes[0]

        ans=max(sizes)+1
        for x0 in range(M):
            for y0 in range(N):
                if grid[x0][y0]==0:
                    temp=set()
                    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                        x1,y1=x0+dx,y0+dy
                        if 0<=x1<M and 0<=y1<N and islands[x1][y1]!=-1:
                            temp.add(islands[x1][y1])
                    ans=max(ans,sum([sizes[island]for island in temp])+1)
        for x in islands:
            print(x)
        print(sizes)
        return ans




grid=[[1, 1], [1, 0]]
grid=[[0,0],[0,0]]
print(Solution().largestIsland(grid))
