# coding=utf-8
'''
Created on 2016å¹?11æœ?18æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = odd_tail = None
        even_head = even_tail = None
        node = head
        odd = True
        while node:
            if odd:
                if odd_head:
                    odd_tail.next = node
                    odd_tail = odd_tail.next
                else:
                    odd_head = odd_tail = node
            else:
                if even_head:
                    even_tail.next = node
                    even_tail = even_tail.next
                else:
                    even_head = even_tail = node
            odd = not odd
            node = node.next
        if odd_tail:
            odd_tail.next = even_head
        if even_tail:
            even_tail.next = None
        return odd_head

