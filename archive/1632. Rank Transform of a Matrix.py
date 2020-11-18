from typing import List
import collections


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        values = collections.defaultdict(list)
        for i in range(M):
            for j in range(N):
                v = matrix[i][j]
                values[v].append((i, j))

        row_rank = [0] * M
        col_rank = [0] * N
        res = [[0] * N for _ in range(M)]

        def find(x):
            path = []
            maxi = uf_rank[x]
            while x != uf[x]:
                path.append(x)
                x = uf[x]
                maxi = max(maxi, uf_rank[x])
            for temp in path:
                uf[temp] = x
                uf_rank[temp] = maxi
            return x

        def connect(x, y):
            root_x, root_y = find(x), find(y)
            uf[root_x] = root_y
            rank = max(uf_rank[root_x], uf_rank[root_y])
            uf_rank[find(x)] = uf_rank[find(y)] = rank

        def get_rank(x):
            return uf_rank[find(x)]

        for v in sorted(values):
            uf = {}
            uf_rank = {}
            for i in range(M):
                uf[(i, None)] = (i, None)
                uf_rank[(i, None)] = 0

            for j in range(N):
                uf[(None, j)] = (None, j)
                uf_rank[(None, j)] = 0

            for i, j in values[v]:
                rank = max(row_rank[i], col_rank[j]) + 1
                uf_rank[find((i, None))] = max(uf_rank[find((i, None))], rank)
                uf_rank[find((None, j))] = max(uf_rank[find((None, j))], rank)
                connect(find((i, None)), find((None, j)))

            for i, j in values[v]:
                rank = get_rank(find((i, None)))
                row_rank[i] = col_rank[j] = res[i][j] = rank

        return res


matrix = [[-37, -50, -3, 44],
          [-37, 46, 13, -32],
          [47, -42, -3, -40],
          [-17, -22, -39, 24]]
print(Solution().matrixRankTransform(matrix))
