# coding=utf-8
'''
Created on 2017å¹?2æœ?15æ—?

@author: Administrator
'''
from data_structure.Link import list_to_list_node, output


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merging(h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    h1 = h1.next
                    tail = tail.next
                else:
                    tail.next = h2
                    h2 = h2.next
                    tail = tail.next
            tail.next = h1 or h2
            return dummy.next

        def sorting(head):
            if head == None or head.next == None:
                return head
            pre = slow = fast = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            h1 = sorting(head)
            h2 = sorting(slow)
            h = merging(h1, h2)
            return h

        return sorting(head)


head = list_to_list_node([4, 3, 2, 1])
print output(Solution().sortList(head))
