class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        visited=set()
        border=[]
        colour=grid[r0][c0]
        def dfs(x,y):
            visited.add((x,y))
            flag=False
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                tx,ty=x+dx,y+dy
                if 0<=tx<len(grid) and 0<=ty<len(grid[0]) and grid[tx][ty]==colour:
                    if (tx,ty) not in visited:
                        dfs(tx,ty)
                else:
                    flag=True
            if flag:
                border.append((x,y))
        dfs(r0,c0)
        for x,y in border:
            grid[x][y]=color
        return grid



