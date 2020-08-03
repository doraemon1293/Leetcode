from typing import List
import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d=collections.defaultdict(dict)
        neighbour=collections.defaultdict(list)
        for a,b in edges:
            neighbour[a].append(b)
            neighbour[b].append(a)

        visited=set()

        def post_order(root):
            res=collections.defaultdict(int)
            res[labels[root]]+=1
            visited.add(root)
            for child in neighbour[root]:
                if child not in visited:
                    res_child=post_order(child)
                    for k in res_child:
                        res[k]+=res_child[k]
            d[root]=res
            return res

        post_order(0)
        ans=[d[i].get(labels[i],0) for i in range(n)]
        return ans
n=4
edges=[[0,2],[0,3],[1,2]]
labels="aeed"
print(Solution().countSubTrees(n,edges,labels))

