from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        p = (0, 0)
        M, N = len(rowSum), len(colSum)
        mat = [[0] * N for _ in range(M)]
        r, c = p
        while r < M and c < N:
            r, c = p
            if rowSum[r] < colSum[c]:
                mat[r][c] = rowSum[r]
                p = (r + 1, c)
                colSum[c] -= rowSum[r]
                rowSum[r] = 0

            elif rowSum[r] > colSum[c]:
                mat[r][c] = colSum[c]
                p = (r, c + 1)
                rowSum[r] -= colSum[c]
                colSum[c] = 0
            else:
                mat[r][c] =rowSum[r]
                rowSum[r] = colSum[c] = 0
                p = (r + 1, c + 1)

            r, c = p
        return mat