# coding=utf-8

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.ans=[]
        N=len(graph)
        def dfs(curNode,prePath):
            if curNode==N-1:
                self.ans.append(prePath)
            else:
                nodes=graph[curNode]
                for node in nodes:
                    dfs(node,prePath+[node])
        dfs(0,[0])
        return self.ans

graph=[[1, 2], [3], [3], []]
graph=[[],[]]
print(Solution().allPathsSourceTarget(graph))

