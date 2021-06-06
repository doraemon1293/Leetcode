# Definition for singly-linked list.


import collections


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        c = collections.Counter()
        p = head
        while p:
            c[p.val] += 1
            p = p.next
        p = ListNode(next=head)
        p0 = p
        while p.next:
            if c[p.next.val] > 1:
                p.next = p.next.next
            else:
                p = p.next
        return p0.next
