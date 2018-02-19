# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            from collections import deque
            current_level = 0
            q = deque()
            q.append((root, 0))
            temp = []
            while q:
                node, level = q.popleft()
                if level > current_level:
                    if current_level % 2 == 0:
                        ans.append(temp)
                    else:
                        ans.append(temp[::-1])
                    temp = []
                    current_level += 1
                temp.append(node.val)
                if node.left:
                    q.append((node.left, current_level + 1))
                if node.right:
                    q.append((node.right, current_level + 1))
            if current_level % 2 == 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            return ans
