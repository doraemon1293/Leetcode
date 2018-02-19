# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def equal(nodea, nodeb):
            if nodea == nodeb == None:
                return True
            elif nodea == None or nodeb == None:
                return False
            else:
                if nodea.val == nodeb.val:
                    return equal(nodea.left, nodeb.left) and equal(nodea.right, nodeb.right)
                else:
                    return False

        def is_part(node, t):
            if equal(node, t):
                return True
            elif node == None or t == None:
                return False
            elif is_part(node.left, t):
                return True
            elif is_part(node.right, t):
                return True
            else:
                return False

        return is_part(s, t)
