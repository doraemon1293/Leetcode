# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow
        p1,p2=mid,mid.next
        mid.next=None
        while p2:
            p3=p2.next
            p2.next=p1
            p1,p2=p2,p3

        p2=p1
        p1=head
        ans=-1
        while p1 and p2:
            ans=max(ans,p1.val+p2.val)
            p1,p2=p1.next,p2.next
        return ans


