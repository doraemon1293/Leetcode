# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursive
        if head and head.next:
            ans = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        else:
            return head
        return ans

        # iterative
#         if head:
#             p, next_p = head, head.next
#             head.next = None
#             while next_p:
#                 temp = next_p.next
#                 next_p.next = p
#                 p, next_p = next_p, temp
#         else:
#             return p

