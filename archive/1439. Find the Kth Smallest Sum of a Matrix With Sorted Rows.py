import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        M, N = len(mat), len(mat[0])
        mini_sum = 0
        for x in range(M):
            mini_sum += mat[x][0]
        heap = [(mini_sum, [0] * M)]
        visited = set()
        visited.add((0,) * M)
        while heap and k:
            summ, seq = heapq.heappop(heap)
            for i in range(M):
                if seq[i] < N - 1:
                    new_seq = list(seq)
                    new_seq[i] += 1
                    new_seq = tuple(new_seq)
                    if new_seq not in visited:
                        temp = mat[i][seq[i] + 1] - mat[i][seq[i]]
                        heapq.heappush(heap, (summ + temp, new_seq))
                        visited.add(new_seq)
            k -= 1
        return summ


mat = [[1, 3, 11], [2, 4, 6]]
k = 5
print(Solution().kthSmallest(mat, k))

#another solution

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
        return h[k-1]