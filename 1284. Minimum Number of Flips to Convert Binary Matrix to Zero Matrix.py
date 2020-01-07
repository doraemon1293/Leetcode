import collections
import copy


class Solution:
    def minFlips(self, mat: list) -> int:
        M, N = len(mat), len(mat[0])
        q = collections.deque()

        def foo(mat):
            return sum([sum(row) for row in mat]), tuple([tuple(row) for row in mat])

        summ, t = foo(mat)
        if summ == 0:
            return 0
        q.append((mat, 0))
        visited = set()
        visited.add(t)

        while q:
            mat, steps = q.popleft()
            for x in range(M):
                for y in range(N):
                    new_mat = copy.deepcopy(mat)
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)):
                        xt, yt = x + dx, y + dy
                        if 0 <= xt < M and 0 <= yt < N:
                            new_mat[xt][yt] = new_mat[xt][yt] ^ 1
                    summ, t = foo(new_mat)
                    if summ == 0:
                        return steps + 1
                    if t not in visited:
                        visited.add(t)
                        q.append((new_mat, steps + 1))
        return -1
mat=[[0,0],[0,1]]
print(Solution().minFlips(mat))