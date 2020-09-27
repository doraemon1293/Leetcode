import collections
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_v=collections.defaultdict(list)
        for from_, to_ in edges:
            in_v[to_].append(from_)
        return len([i for i in range(n) if in_v[i]==0])
