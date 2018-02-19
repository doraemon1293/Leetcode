# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        q = head
        while l1 and l2:
            if l1.val < l2.val:
                p = ListNode(l1.val)
                q.next = p
                q = p
                l1 = l1.next
            else:
                p = ListNode(l2.val)
                q.next = p
                q = p
                l2 = l2.next
        if l1 == None:
            q.next = l2
        if l2 == None:
            q.next = l1
        head = head.next
        return head

