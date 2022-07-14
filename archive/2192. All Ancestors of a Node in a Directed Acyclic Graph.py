from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        G1 = [set() for i in range(n)]
        G2 = [set() for i in range(n)]  # r_g
        for a, b in edges:
            G1[a].add(b)
            G2[b].add(a)
        ans = [set() for _ in range(n)]
        not_visited = set(range(n))
        while not_visited:
            zeros = set([node for node in not_visited if len(G2[node]) == 0])
            for node in zeros:
                for node1 in G1[node]:
                    ans[node1].add(node)
                    ans[node1]|=ans[node]
                    G2[node1].remove(node)
            not_visited -= zeros
            # print(zeros)
            # print(not_visited)
        ans = [sorted(arr) for arr in ans]
        return ans
n=8
e=[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(Solution().getAncestors(n,e))