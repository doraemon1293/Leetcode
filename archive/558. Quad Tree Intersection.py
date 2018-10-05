"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        elif quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
        else:
            topLeft=self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            topRight=self.intersect(quadTree1.topRight,quadTree2.topRight)
            bottomLeft=self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            bottomRight=self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val==topRight.val==bottomLeft.val==bottomRight.val:
                return Node(topLeft.val,True,None,None,None,None)
            else:
                return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)