# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        d = {}
        d[0] = 0
        arr = [(0, dummy)]
        summ = 0
        p = head
        while p:
            if p.val==0:
                temp_p=arr[-1][1]
                p=p.next
                temp_p.next=p
            else:
                summ += p.val
                if summ in d:
                    ind=d[summ]
                    for i in range(ind+1,len(arr)):
                        temp_sum=arr[i][0]
                        del d[temp_sum]
                    arr=arr[:ind+1]
                    p=p.next
                    arr[-1][1].next=p
                else:
                    arr.append((summ, p))
                    d[summ] = len(arr) - 1
        return dummy.next
