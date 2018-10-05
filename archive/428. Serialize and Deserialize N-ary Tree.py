"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root is None:
            return ""
        q = []

        def preorder(root):
            if root is None:
                return None
            else:
                q.append(root.val)
                for child in root, children:
                    preorder(child)
                q.append("#")

        preorder(root)
        return ",".join(map(str, q))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == "":
            return None
        data = deque(data.split(","))
        root = Node(int(data.popleft()), [])

        def solve(root):
            val = data.popleft()
            while val != '#':
                child = Node(int(val, []))
                solve(child)
                root.children.append(child)
                val = data.popleft()

        solve(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
