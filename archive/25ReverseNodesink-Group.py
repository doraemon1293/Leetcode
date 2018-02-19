# coding=utf-8
'''
Created on 2016å¹?12æœ?15æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def output(head):
    ans = []
    p = head
    while p != None:
        ans.append(p.val)
        p = p.next
    return ans


def list_to_list_node(a):
    head = ListNode(0)
    p = head
    for i in range(len(a)):
        p.val = a[i]
        if i < len(a) - 1:
            p.next = ListNode(0)
            p = p.next
    return head


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        last_group_tail = dummy
        cur_head = cur_tail = head
        while cur_tail:
            temp_k = k - 1
            while cur_tail and temp_k:
                cur_tail = cur_tail.next
                temp_k -= 1
            if cur_tail:
                next_group_head = cur_tail.next
                p = cur_head
                new_p = next_group_head
                for _ in xrange(k):
                    p.next, p, new_p = new_p, p.next, p
                last_group_tail.next = cur_tail
                last_group_tail = cur_head
                cur_head = cur_tail = next_group_head
        return dummy.next


head = list_to_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
k = 3
print output(Solution().reverseKGroup(head, k))
