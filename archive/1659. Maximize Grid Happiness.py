import sys

"""
We just traverse all the possibilities but we should early stop under the following cases:

when the rest of the people cannot exceeds the current max happiness even when they are in the optimistic states (E.g. 120 for introverts and 160 for extraverts)
we should never leave a grid unoccupied, if this grid's up and left neighbors are unoccupied.
An upvote would be incredibly helpful if you find this post interesting.
"""
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        sys.setrecursionlimit(10 ** 6)
        self.max_score = 0
        grid = [[""] * n for _ in range(m)]

        def put(x, y, ch, score):
            if ch == "I":
                grid[x][y] = "I"
                new_score = score + 120
                for x0, y0 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= x0 < m and 0 <= y0 < n:
                        if grid[x0][y0] == "I":
                            new_score -= 30
                            new_score -= 30
                        elif grid[x0][y0] == "E":
                            new_score -= 30
                            new_score += 20
                return new_score
            if ch == "E":
                grid[x][y] = "E"
                new_score = score + 40
                for x0, y0 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= x0 < m and 0 <= y0 < n:
                        if grid[x0][y0] == "I":
                            new_score += 20
                            new_score -= 30
                        elif grid[x0][y0] == "E":
                            new_score += 20
                            new_score += 20
                return new_score

        def next_xy(x, y):
            y += 1
            x += y // n
            y = y % n
            return x, y

        def dfs(x, y, introvertsCount, extrovertsCount, score):
            # print(x, y, introvertsCount, extrovertsCount, new_score)
            # for row in grid:
            #     print(row)
            if x == m:
                return
            if score+introvertsCount*120+extrovertsCount*160<=self.max_score:
                return
            else:
                x1, y1 = next_xy(x, y)
                if grid[x][y] == "":
                    if introvertsCount:
                        new_score = put(x, y, "I", score)
                        self.max_score = max(self.max_score, new_score)
                        dfs(x1, y1, introvertsCount - 1, extrovertsCount, new_score)
                        grid[x][y] = ""
                    if extrovertsCount:
                        new_score = put(x, y, "E", score)
                        self.max_score = max(self.max_score, new_score)
                        dfs(x1, y1, introvertsCount, extrovertsCount - 1, new_score)
                        grid[x][y] = ""
                if 0<=x-1<m and 0<=y<n and grid[x-1][y]!="" or 0<=x<m and 0<=y-1<n and grid[x][y-1]!="":
                    dfs(x1, y1, introvertsCount, extrovertsCount, score)

        dfs(0, 0, introvertsCount, extrovertsCount, 0)
        return self.max_score

print(Solution().getMaxGridHappiness(5,5,6,6))