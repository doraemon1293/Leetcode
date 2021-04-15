import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(set)
        for a, b in adjacentPairs:
            adj[a].add(b)
            adj[b].add(a)
        # print(adj)
        head, tail = [k for k in adj if len(adj[k]) == 1]
        arr = [head]
        p = head
        while p != tail:
            new = adj[p].pop()
            adj[new].remove(p)
            p = new
            arr.append(p)
        return arr
print(Solution().restoreArray( adjacentPairs = [[2,1],[3,4],[3,2]]))