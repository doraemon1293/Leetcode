class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def height(root):
            if root==None:
                return 0
            else:
                maxi=max(map(height,root.children)+[0])
                return 1+maxi
        return height(root)