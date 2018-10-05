"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        def solve(head):
            node = tail = head
            while node:
                if node.child:
                    child_head, child_tail = solve(node.child)
                    temp = node.next
                    node.next = child_head
                    child_head.prev = node
                    child_tail.next = temp
                    if temp:
                        temp.prev = child_tail
                        tail = temp
                    else:
                        tail = child_tail
                    node.child = None
                    node = temp

                else:
                    tail = node
                    node = node.next
            return head, tail

        res_head, res_tail = solve(head)
        return res_head
