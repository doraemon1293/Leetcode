# coding=utf-8
'''
Created on 2016å¹?11æœ?3æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while p1.next and p1.next.next:
            p2, p3, p4 = p1.next, p1.next.next, p1.next.next.next
            p1.next, p2.next, p3.next = p3, p4, p2
            p1 = p2
        return dummy.next


head = list_to_list_node([1, 2, 3, 4])
print output(Solution().swapPairs(head))
