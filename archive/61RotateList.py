# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        k = k % length
        if k == 0: return head
        p = head
        for _ in xrange(length - k):
            p = p.next
        new_head = p
        print new_head.val
        while p.next:
            p = p.next
        p.next = head
        p = head
        while p.next != new_head:
            p = p.next
        p.next = None
        return new_head
