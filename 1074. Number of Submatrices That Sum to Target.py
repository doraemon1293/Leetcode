class Solution:
    def numSubmatrixSumTarget(self, matrix: list, target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        pre_sum = []
        for i in range(M):
            summ = 0
            pre_sum.append([])
            for j in range(N):
                summ += matrix[i][j]
                pre_sum[i].append(summ)
        ans = 0
        for left in range(N):
            for right in range(left, N):
                d = {0: 1}
                summ = 0
                for row in range(M):
                    summ += pre_sum[row][right] - (pre_sum[row][left - 1] if left - 1 >= 0 else 0)
                    ans += d.get(summ-target, 0)
                    d.setdefault(summ, 0)
                    d[summ] += 1
        return ans


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target))
