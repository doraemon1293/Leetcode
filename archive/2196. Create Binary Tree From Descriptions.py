# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        d = {}
        childern = set()
        for p, c, isleft in descriptions:
            d.setdefault(p, [None, None])
            if isleft:
                d[p][0] = c
            else:
                d[p][1] = c
            childern.add(c)
        root_val = [node for node in d if node not in childern][0]

        def construct(val):
            node = TreeNode(val=val) if val!=None else None
            if val in d:
                node.left = construct(d[val][0])
                node.right = construct(d[val][1])
            return node

        root=construct(root_val)

        return root
desc=[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

print(Solution().createBinaryTree(desc))