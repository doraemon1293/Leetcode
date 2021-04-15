# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p=list1
        for _ in range(a-1):
            p=p.next
        p1=p
        for _ in range(b-a+2):
            p=p.next
        p2=p
        p=list2
        while p.next:
            p=p.next
        list2_end=p
        p1.next=list2
        list2_end.next=p2
        return list1
