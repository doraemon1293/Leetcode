# coding=utf-8
'''
Created on 2017å¹?1æœ?12æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head

        def foo(p):
            if p.next == None:
                temp = p.val + 1
                p.val = temp % 10
                return temp / 10
            else:
                temp = p.val + foo(p.next)
                p.val = temp % 10
                return temp / 10

        temp = foo(head)
        if temp == 1:
            p = ListNode(temp)
            p.next = head
            head = p
        return head
