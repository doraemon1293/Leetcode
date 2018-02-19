# coding=utf-8
'''
Created on 2017å¹?7æœ?28æ—?

@author: Administrator
'''
from data_structure.Link import list_to_list_node, output


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        p = head.next
        tail = head
        tail.next = None
        while p:
            next_p = p.next
            if p.val < head.val:
                p.next = head
                head = p
            else:
                temp_p = head
                while temp_p.next and temp_p.next.val <= p.val:
                    temp_p = temp_p.next
                p.next = temp_p.next
                temp_p.next = p
            p = next_p
        return head


head = list_to_list_node([1, 2, 34, ])
print output(Solution().insertionSortList(head))
