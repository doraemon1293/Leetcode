"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if root is None:
            return None
        ret_root = TreeNode(root.val)
        if root.children:
            ret_root.left = self.encode(root.children[0])
            node = ret_root.left
            for child in root.children[1:]:
                node.right = self.encode(child)
                node = node.right
        return ret_root

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        root = data
        if root is None:
            return None
        ret_root = Node(root.val, [])
        node = root.left
        while node:
            ret_root.children.append(self.decode(node))
            node = node.right
        return ret_root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
