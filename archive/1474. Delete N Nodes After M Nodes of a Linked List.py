# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        p=ListNode(0)
        p.next=head
        while p:
            #jump m
            _m=m
            while p and _m:
                _m-=1
                p=p.next
            if p:
                #delete n
                _n=n
                while p.next and _n:
                    _n-=1
                    p.next=p.next.next
        return head

