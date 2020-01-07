class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        starts = []
        for y in range(N):
            if A[0][y] == 1:
                starts.append((0, y))
            if A[M - 1][y] == 1:
                starts.append((M - 1, y))
        for x in range(M):
            if A[x][0] == 1:
                starts.append((x, 0))
            if A[x][N - 1] == 1:
                starts.append((x, N - 1))

        def dfs(x, y):
            if A[x][y] == 1:
                A[x][y] = 2
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < M and 0 <= ty < N:
                        dfs(tx, ty)

        for x, y in starts:
            dfs(x, y)
        ans = 0
        for x in range(M):
            for y in range(N):
                if A[x][y] == 1:
                    ans += 1
        return ans
