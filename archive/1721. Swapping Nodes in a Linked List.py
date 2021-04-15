
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p=head
        temp=k-1
        while temp:
            p=p.next
            temp-=1
        p1=p

        p=head
        n=0
        while p:
            n+=1
            p=p.next

        p=head
        temp=(n-k)
        while temp:
            p=p.next
            temp-=1
        p2=p
        p1.val,p2.val=p2.val,p1.val
        return head