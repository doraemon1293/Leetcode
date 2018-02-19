# coding=utf-8
'''
Created on 2017å¹?8æœ?30æ—?

@author: Administrator
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        p = head
        while p:
            if p in s:
                return p
            else:
                s.add(p)
                p = p.next
        return None
