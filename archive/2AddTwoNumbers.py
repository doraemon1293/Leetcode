# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

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
        head = ListNode(0)
        add = 0
        p = head
        while l1 != None or l2 != None:
            temp = add
            if l1 != None:
                temp += l1.val
                l1 = l1.next
            if l2 != None:
                temp += l2.val
                l2 = l2.next
            add = temp / 10
            temp = temp % 10
            print add, temp
            p.val = temp
            if l1 != None or l2 != None or add == 1:
                p.next = ListNode(add)
                p = p.next
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


p1 = list_to_list_node([2, 4, 5])
p2 = list_to_list_node([5, 6, 4])

print output(Solution().addTwoNumbers(p1, p2))

