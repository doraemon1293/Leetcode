from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        memo = {}
        M, N = len(grid), len(grid[0])
        avai = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "#":
                    pass
                else:
                    avai += 1
                    if grid[i][j] == "C":
                        cat = (i, j)
                    if grid[i][j] == "M":
                        mouse = (i, j)
                    if grid[i][j] == "F":
                        food = (i, j)

        def dfs(turns, cat, mouse):
            # print(turns, cat, mouse)
            # print(memo.get((turns % 2, cat, mouse),None))
            if turns > avai * 2:
                return "Cat"
            if cat == mouse:
                return "Cat"
            if cat == food:
                return "Cat"
            if mouse == food:
                return "Mouse"
            if (turns, cat, mouse) in memo:
                return memo[(turns, cat, mouse)]
            if turns % 2 == 0:
                # mouse's turn
                x, y = mouse
                if dfs(turns + 1, cat, mouse) == "Mouse":
                    memo[turns, cat, mouse] = "Mouse"
                    return "Mouse"

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    for step in range(1, mouseJump + 1):
                        x1, y1 = x + dx * step, y + dy * step
                        if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] != "#":
                            temp = dfs(turns + 1, cat, (x1, y1))
                            if temp == "Mouse":
                                memo[turns, cat, mouse] = "Mouse"
                                return "Mouse"
                        else:
                            break
                memo[turns, cat, mouse] = "Cat"
                return "Cat"
            else:
                # cat's turn
                x, y = cat
                if dfs(turns + 1, cat, mouse) == "Cat":
                    memo[turns, cat, mouse] = "Cat"
                    return "Cat"
                for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    for step in range(1, catJump + 1):
                        x1, y1 = x + dx * step, y + dy * step
                        if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] != "#":
                            temp = dfs(turns + 1, (x1, y1), mouse)
                            if temp == "Cat":
                                memo[turns, cat, mouse] = "Cat"
                                return "Cat"
                        else:
                            break
                memo[turns, cat, mouse] = "Mouse"
                return "Mouse"

        # dfs(0, cat, mouse)
        # for k in sorted(memo):
        #     print(k, memo[k])
        if dfs(0, cat, mouse)=="Mouse":
            return True
        else:
            return False


print(Solution().canMouseWin(grid=["####F",
                                   "#C...",
                                   "M...."], catJump=1, mouseJump=2))
