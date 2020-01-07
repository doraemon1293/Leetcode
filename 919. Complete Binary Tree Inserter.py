# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [root]
        for node in self.nodes:
            if node.left: self.nodes.append(node.left)
            if node.right: self.nodes.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self.nodes.append(node)
        n = len(self.nodes) - 1
        p = self.nodes[(n - 1) / 2]
        if n % 2:
            p.left = node
        else:
            p.right = node
        return p.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
