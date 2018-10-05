"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None: return []
        cur_level = [root]
        ans = []
        while cur_level:
            ans.append([node.val for node in cur_level])
            temp = []
            for node in cur_level:
                temp += [x for x in (node.children) if x != None]
            cur_level = temp
        return ans

