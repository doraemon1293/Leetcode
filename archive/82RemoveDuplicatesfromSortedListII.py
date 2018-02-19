# coding=utf-8
'''
Created on 2017å¹?8æœ?17æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p:
            if p.next and p.next.next and p.next.val == p.next.next.val:
                q = p.next.next
                while q and q.val == p.next.val:
                    q = q.next
                p.next = q
            else:
                p = p.next
        return dummy.next

