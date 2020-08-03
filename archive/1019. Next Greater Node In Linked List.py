# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        p1 = head
        while p1:
            p1.gval = 0
            while stack and stack[-1].val < p1.val:
                p = stack.pop()
                p.gval = p1.val
            stack.append(p1)
            p1 = p1.next
        ans = []
        p1 = head
        while p1:
            ans.append(p1.gval)
            p1 = p1.next
        return ans
