# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        while p and p.val == val:
            p = p.next
        head = p
        if head:
            while p.next:
                if p.next.val == val:
                    p.next = p.next.next
                else:
                    p = p.next
        return head

