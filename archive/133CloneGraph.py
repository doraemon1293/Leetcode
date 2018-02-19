# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''


# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None
        nodeCopy = UndirectedGraphNode(node.label)
        d = {node:nodeCopy}
        from collections import deque
        q = deque([node])
        while q:
            node = q.popleft()
            for nNode in node.neighbors:
                if nNode in d:
                    d[node].neighbors.append(d[nNode])
                else:
                    nNodeCopy = UndirectedGraphNode(nNode.label)
                    d[nNode] = nNodeCopy
                    d[node].neighbour.append(nNodeCopy)
                    q.append(nNodeCopy)
        return nodeCopy

