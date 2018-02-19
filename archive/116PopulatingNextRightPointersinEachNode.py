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
        if root:
            cur = most_left_node = root
            while most_left_node.left:
                cur = most_left_node
                while cur:
                    cur.left.next = cur.right
                    cur.right.next = cur.next.left if cur.next else None
                    cur = cur.next
                most_left_node = most_left_node.left
