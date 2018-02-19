# Definition for a binary tree node.
from data_structure.Tree import list_to_tree


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        from collections import deque, defaultdict
        q = deque([root])
        sourceNode = None
        edges = defaultdict(set)
        while q:
            node = q.popleft()
            if node.val == k:
                sourceNode = node
            if node.left:
                edges[node].add(node.left)
                edges[node.left].add(node)
                q.append(node.left)
            if node.right:
                edges[node].add(node.right)
                edges[node.right].add(node)
                q.append(node.right)

        q = deque([sourceNode])
        visited = set()
#         print sourceNode.val
#         for u in edges:
#             for v in edges[u]:
#                 print u.val, v.val
        while q:
            u = q.popleft()
            visited.add(u)
            if u.left == u.right == None:
                return u.val
            for v in edges[u]:
                if v not in visited:
                    q.append(v)


root = list_to_tree([1, 3, 2])
# root = list_to_tree([1])

k = 1
print Solution().findClosestLeaf(root, k)
