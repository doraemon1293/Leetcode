"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head==None:
            node=Node(insertVal,None)
            node.next=node
            return node
        else:
            node=head
            new_node=Node(insertVal,None)
            while 1:
                if node.val<=insertVal<=node.next.val or (node.val>node.next.val and (insertVal>=node.val or insertVal<=node.next.val)) or node.next==head:
                    new_node.next=node.next
                    node.next=new_node
                    break
                node=node.next

            return head
