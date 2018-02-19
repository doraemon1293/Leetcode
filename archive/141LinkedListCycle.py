# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        p = head
        while p and p not in s:
            s.add(p)
            p = p.next
        return bool(p)

