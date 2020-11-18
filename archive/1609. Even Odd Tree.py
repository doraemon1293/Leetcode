# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        cur_level = [root]
        level = 0
        while cur_level:
            temp = [node.val for node in cur_level]
            for i in range(len(temp) - 1):
                if level % 2 == 0 and temp[i] >= temp[i + 1]:
                    return False
                if level % 2 == 1 and temp[i] <= temp[i + 1]:
                    return False
            temp = [x for x in temp if (x + level) % 2 == 0]
            if temp:
                return False
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
            level += 1
        return True

