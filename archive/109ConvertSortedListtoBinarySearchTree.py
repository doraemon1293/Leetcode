# coding=utf-8
'''
Created on 2017å¹?7æœ?26æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def foo(st, en):
            if st > en:
                return None
            else:
                mid = (st + en) / 2
                left = foo(st, mid - 1)
                root = TreeNode(self.node.val)
                self.node = self.node.next
                root.left = left
                right = foo(st, mid + 1)
                root.right = right
                return root

        length, p = 0, head
        while p:
            length += 1
            p = p.next
        self.node = head
        return foo(0, length - 1)

