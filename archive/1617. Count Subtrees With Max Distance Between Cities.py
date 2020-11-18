from typing import List
import collections


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:

        def get_depth(e_, node):
            self.visited.add(node)
            arr = []
            for child in e_[node]:
                if child not in self.visited:
                    depth = get_depth(e_, child)
                    arr.append(depth)
            arr.sort(reverse=True)
            if len(arr) == 0:
                return 0
            else:
                if len(arr) == 1:
                    self.max_dis = max(self.max_dis, arr[0] + 1)
                elif len(arr) > 1:
                    self.max_dis = max(self.max_dis, arr[0] + arr[1] +2)
                return arr[0] + 1

        e = collections.defaultdict(set)
        for s, t in edges:
            s -= 1
            t -= 1
            e[s].add(t)
            e[t].add(s)

        ans = [0] * n
        for state in range(1, 2 ** n):
            nodes = set([i for i in range(n) if (state >> i) & 1])
            e_ = collections.defaultdict(set)
            for node in nodes:
                e_[node] = e[node] & nodes
            self.max_dis = 0
            self.visited = set()
            get_depth(e_, node)
            if len(self.visited) == len(nodes):
                # print(nodes, self.max_dis, self.visited)
                # print(e_)
                ans[self.max_dis] += 1
        # print(ans)

        return ans[1:]


n = 4
edges = [[1, 2], [2, 3], [2, 4]]
n=4
edges=[[1,3],[1,4],[2,3]]
print(Solution().countSubgraphsForEachDiameter(n, edges))
