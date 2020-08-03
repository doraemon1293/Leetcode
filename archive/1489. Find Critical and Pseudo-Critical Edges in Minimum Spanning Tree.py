from typing import List
import heapq
import collections


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # get total_weight of MST
        # for each edge
        # delete a edge if total_weight1>total_weight or no MST => this edge is critical
        # if this edge is not critical edge, include this edge firstly, generate MST, if weight==total_weight this edge is Pseudo-Critical
        self.edges = edges
        self.n = n

        def gen_MST(neighbours, deleted_edge, added_edge):
            if added_edge != None:
                s1, s2, weight = self.edges[added_edge]
                visited = {s1, s2}
                mst_weight = weight
            else:
                visited = {0}
                mst_weight = 0
            nodes_heap = []

            for node in visited:
                for to, weight, edge_ind in neighbours[node]:
                    if edge_ind != deleted_edge and to not in visited:
                        nodes_heap.append([weight, to, edge_ind])
            heapq.heapify(nodes_heap)

            while len(visited) < self.n and nodes_heap:
                new_weight, new_node, new_edge_ind = heapq.heappop(nodes_heap)
                if new_node not in visited:
                    visited.add(new_node)
                    mst_weight += new_weight
                    for to, weight, edge_ind in neighbours[new_node]:
                        if edge_ind != deleted_edge and to not in visited:
                            heapq.heappush(nodes_heap, [weight, to, edge_ind])
            if len(visited) == self.n:
                return mst_weight
            else:
                return float("inf")

        neighbours = collections.defaultdict(list)
        for i in range(len(edges)):
            fromi, toi, weighti = edges[i]
            neighbours[fromi].append((toi, weighti, i))
            neighbours[toi].append((fromi, weighti, i))

        min_mst_weight = gen_MST(neighbours, None, None)
        critical_edges=[]
        pseudo_critical_edges=[]
        for ind in range(len(edges)):
            deleted_one_edge_mst_weigh=gen_MST(neighbours,ind,None)
            if deleted_one_edge_mst_weigh>min_mst_weight:
                critical_edges.append(ind)
            else:
                added_one_edge_mst_weight=gen_MST(neighbours,None,ind)
                if added_one_edge_mst_weight==min_mst_weight:
                    pseudo_critical_edges.append(ind)
        return [critical_edges, pseudo_critical_edges]



n = 5
edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))
