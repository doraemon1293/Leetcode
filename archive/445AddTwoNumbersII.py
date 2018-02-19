# coding=utf-8
'''
Created on 2016å¹?11æœ?28æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        s_ans = []
        add = 0
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        while s1 or s2 or add:
            if s1:
                t1 = s1.pop()
            else:
                t1 = 0
            if s2:
                t2 = s2.pop()
            else:
                t2 = 0
            print t1, t2
            s_ans.append((t1 + t2 + add) % 10)
            add = (t1 + t2 + add) / 10
        ans = ListNode(0)
        p = ans
        while s_ans:
            p.next = ListNode(s_ans.pop())
            p = p.next
        ans = ans.next
        return ans


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


l1 = list_to_list_node([5])
l2 = list_to_list_node([5])
print output(Solution().addTwoNumbers(l1, l2))

