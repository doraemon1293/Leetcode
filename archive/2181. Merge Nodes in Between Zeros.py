# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        new_head=new_tail=None
        summ=None

        while p:
            if p.val==0:
                if summ==None:
                    summ=0
                else:
                    if new_head:
                        new_head=new_tail=ListNode(summ)
                    else:
                        new_tail.next=ListNode(summ)
                        new_tail=new_tail.next
                    summ=0
            else:
                summ+=p.val
            p=p.next
        return new_head

