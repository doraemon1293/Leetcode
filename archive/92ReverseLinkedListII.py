# coding=utf-8
'''
Created on 2017å¹?1æœ?10æ—?

@author: Administrator
'''
from data_structure.Link import list_to_list_node, output
from data_structure.Tree import list_to_tree


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # head1->tail1->nth_node->mth_node->head2->tail2
        times = n - m
        tail1 = None
        p = head
        while m - 1 > 0:
            tail1 = p
            p = p.next
            m -= 1
        mth_node = p
        p1, p2 = mth_node, mth_node.next
        while times > 0:
            new_p1 = p2
            new_p2 = p2.next
            p2.next = p1
            p1, p2 = new_p1, new_p2
            times -= 1
        mth_node.next = p2
        if tail1:
            tail1.next = p1
        else:
            head = p1
        return head


arr = [1, 2, 3, 4, 5]
arr = [1]
head = list_to_list_node(arr)
print output(Solution().reverseBetween(head, 1, 1))
