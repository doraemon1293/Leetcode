# coding=utf-8
'''
Created on 2017å¹?1æœ?4æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree, tree_to_list


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
        from collections import deque
        if root == None: return ""
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
        return ",".join([str(x) for x in ans])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        if data == "": return None
        arr = [None if x == "None" else x for x in data.split(",")]
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


arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, None]
codec = Codec()

root = list_to_tree(arr)
print tree_to_list(codec.deserialize(codec.serialize(root)))
