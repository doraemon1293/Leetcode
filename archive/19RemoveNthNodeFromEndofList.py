# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p2 = head
        p1 = head
        for _ in range(n):
            p2 = p2.next
        if p2 == None:
            head = head.next
            return head
        else:
            while p2.next:
                p1 = p1.next
                p2 = p2.next
            p1.next = p1.next.next
            return head


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


print output(Solution().removeNthFromEnd(list_to_list_node([1]), 1))

