# coding=utf-8
'''
Created on 2016å¹?11æœ?14æ—?

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            mid = slow = fast = head
            second_half = mid.next
            next_slow = mid.next
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = next_slow
                next_slow = slow.next
                temp = mid
                mid = slow
                second_half = mid.next
                mid.next = temp

            first_half = mid
            if not fast.next:
                first_half = first_half.next
            while first_half and second_half and first_half.val == second_half.val:
                first_half, second_half = first_half.next if first_half != head else None, second_half.next
                print first_half.val, second_half.val
            if first_half == None:
                return True
            else:
                return False
        else:
            return True


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


head = list_to_list_node([1, 2])
print Solution().isPalindrome(head)

