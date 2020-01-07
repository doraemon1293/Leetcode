# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        arr = [root]
        level = 0
        should_be_last_level=False
        while arr:
            level += 1
            new_arr = []
            none_in_new_arr = False
            for node in arr:
                for new_node in (node.left, node.right):
                    if new_node:
                        if should_be_last_level:
                            return False
                        if none_in_new_arr:
                            return False
                        else:
                            new_arr.append(new_node)
                    else:
                        none_in_new_arr = True
                        should_be_last_level=True
            arr = new_arr
        return True
