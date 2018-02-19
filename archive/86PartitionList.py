# coding=utf-8
'''
Created on 2017å¹?6æœ?17æ—?

@author: Administrator
'''
from data_structure.Link import list_to_list_node, output


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_p = small_head = ListNode(0)
        big_p = big_head = ListNode(0)
        p = head
        while p:
            print p.val
            if p.val < x:
                small_p.next = p
                small_p = p
            else:
                big_p.next = p
                big_p = p
            p = p.next
        big_head = big_head.next
        small_p.next = big_head
        big_p.next = None
        small_head = small_head.next
        return small_head


head = list_to_list_node([])
x = 4
print output(Solution().partition(head, x))
