from typing import List


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
                return x
            path = []
            while uf[x] != x:
                path.append(x)
                x = uf[x]
            for y in path:
                uf[y] = x
            return x

        def connect(a, b):
            uf[find(a)] = find(b)

        ans = [None] * len(queries)
        queries = sorted([(i, q) for i, q in enumerate(queries)], key=lambda x: x[1][2])
        edgeList.sort(key=lambda x: x[2])
        ind = 0
        for i, q in queries:
            u, v, limit = q
            while ind < len(edgeList) and edgeList[ind][2] < limit:
                a, b = edgeList[ind][0], edgeList[ind][1]
                connect(a, b)
                ind += 1
            ans[i]=(find(u)==find(v))
        return ans

print(Solution().distanceLimitedPathsExist(n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]))