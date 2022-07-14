# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head=PolyNode(0,0,None)
        p=head
        while poly1 and poly2:
            if poly1.power>poly2.power:
                coef,power=poly1.coefficient,poly1.power
                poly1=poly1.next
            elif poly2.power>poly1.power:
                coef, power = poly2.coefficient, poly2.power
                poly2 = poly2.next
            else:
                coef,power=poly1.coefficient+poly2.coefficient,poly1.power
                poly1,poly2=poly1.next,poly2.next
            if coef:
                p.next=PolyNode(coef,power)
                p=p.next
        if poly1:
            p.next=poly1
        if poly2:
            p.next=poly2
        return head.next



