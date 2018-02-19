# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
         """
        ans = []
        for lst in lists:
            while lst:
                ans.append(lst.val)
                lst = lst.next
        ans.sort()
        if ans:
            head = ListNode(0)
            p = head
            for num in ans:
                q = ListNode(num)
                p.next = q
                p = q
            return head.next
        else:
            return None


def output(head):
    ans = []
    p = head
    while p != None:
        ans.append(p.val)
        p = p.next
    return ans


def list_to_list_node(a):
    if a:
        head = ListNode(0)
        p = head
        for i in range(len(a)):
            p.val = a[i]
            if i < len(a) - 1:
                p.next = ListNode(0)
                p = p.next
        return head
    else:
        return None


lists = [None] * 3
lists[0] = list_to_list_node([2, 3, 5])
lists[1] = list_to_list_node([4, 5, 6])
lists[2] = list_to_list_node([])
print output(Solution().mergeKLists(lists))

