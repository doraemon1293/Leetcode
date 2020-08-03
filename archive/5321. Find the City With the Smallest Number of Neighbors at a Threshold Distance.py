class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        mat = [[float("inf")] * n for _ in range(n)]
        for i, j, w in edges:
            mat[i][j] = mat[j][i] = w
        for i in range(n):
            mat[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        min_count = float("inf")
        ans = None
        for i in range(n):
            count = 0
            for j, dis in enumerate(mat[i]):
                if dis <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                ans = max(ans, i)
        return ans
