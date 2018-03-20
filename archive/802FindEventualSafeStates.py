class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        outZeroVs=[]
        ans=set()
        d=defaultdict(set)
        inDegree=[]
        for i in range(len(graph)):
            if len(graph[i])==0:
                outZeroVs.append(i)
            inDegree.append(len(graph[i]))
            for v in graph[i]:
                d[v].add(i)
        while outZeroVs:
            v=outZeroVs.pop()
            ans.add(v)
            for v1 in d[v]:
                inDegree[v1]-=1
                if inDegree[v1]==0:
                    outZeroVs.append(v1)
        return sorted(list(ans))

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution().eventualSafeNodes(graph))



