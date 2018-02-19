# coding=utf-8
'''
Created on 2016å¹?12æœ?12æ—?

@author: Administrator
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        def find_next_node(cur, position):
            while cur:
                if position == "left":
                    if cur.right:
                        return cur.right, cur
                    else:
                        position = "right"
                elif position == "right":
                    cur = cur.next
                    if cur and cur.left:
                        return cur.left, cur
                    else:
                        position = "left"
            return None, None

        if root:
            cur = root
            while cur:
                most_left = None
                while cur:
                    if cur.left and cur.left.next == None:
                        if most_left == None:
                            most_left = cur.left
                        cur.left.next, cur = find_next_node(cur, "left")
                    elif cur.right:
                        if most_left == None:
                            most_left = cur.right
                        cur.right.next, cur = find_next_node(cur, "right")
                    else:
                        cur = cur.next
                cur = most_left

