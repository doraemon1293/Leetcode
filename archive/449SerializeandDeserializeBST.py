# coding=utf-8
'''
Created on 2017å¹?5æœ?26æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def tree_to_list(root):
            from collections import deque
            if root == None: return []
            ans = []
            q = deque([root])
            while len(q) != 0:
                node = q.popleft()
                ans.append(node.val if node else None)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            while ans[-1] == None:
                del ans[-1]
            return ans

        return str(tree_to_list(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: stra
        :rtype: TreeNode
        """

        def list_to_tree(arr):
            from collections import deque
            if arr == [] or arr[0] == None:
                return None
            root = TreeNode(arr[0])
            q = deque([root])
            l_r = "left"
            for x in arr[1:]:
                node = None if x == None else TreeNode(x)
                if l_r == "left":
                    q[0].left = node
                    if node != None: q.append(node)
                    l_r = "right"
                else:
                    q[0].right = node
                    if node != None: q.append(node)
                    q.popleft()
                    l_r = "left"
            return root

        return list_to_tree(eval(data))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
