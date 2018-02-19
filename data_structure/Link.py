# coding=utf-8
'''
Created on 2016å¹?12æœ?13æ—?

@author: Administrator
'''


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
    p = head = ListNode(0)
    for i in range(len(a)):
        p.next = ListNode(a[i])
        p = p.next
    head = head.next
    return head
