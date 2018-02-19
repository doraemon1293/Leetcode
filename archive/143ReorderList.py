# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''
from data_structure.Link import list_to_list_node, output


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None: return head
        # Half
        last = slow = fast = head
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        if last != slow:
            last.next = None
        middle = slow  # even: 0,1,2,3,4,5 middle in 3/ 0,5,1,4,2,3
                       # odd: 0,1,2,3,4 middle in 3/ 0,4,1,3,2
#         print output(head)
#         print output(middle)
        # reverse middle
        p1, p2 = None, middle
        while p2:
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        middle = p1
        # merge
        head_1, head_2 = head, middle
        p1, p2 = head_1, head_2
        while p1 and p2:
            next_p1, next_p2 = p1.next, p2.next
            p1.next = p2
            p2.next = next_p1 if next_p1 != None else p2.next
            p1, p2 = next_p1, next_p2


head = list_to_list_node([0, 1, 2, 3, 4, 5, 6, 7, 8])
# head = list_to_list_node([0, 1])

Solution().reorderList(head)
print output(head)
