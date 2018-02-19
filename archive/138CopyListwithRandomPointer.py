# coding=utf-8
'''
Created on 2016å¹?11æœ?28æ—?

@author: Administrator
'''


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# hash table method
# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: RandomListNode
#         :rtype: RandomListNode
#         """
#         p = head
#         node_random = {}
#         node_label = {}
#         ans = RandomListNode(0)
#         copy_p = ans
#         while p:
#             temp = RandomListNode(p.label)
#             copy_p.next = temp
#             node_label[p.label] = temp
#             node_random[p.label] = p.random.label if p.random else None
#             copy_p = copy_p.next
#             p = p.next
#         ans = ans.next
#         p = ans
#         while p:
#             p.random = node_label[node_random[p.label]] if node_random[p.label] != None else None
#             p = p.next
#         return ans


# No extra space cost
class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        copy_head = RandomListNode(0)
        copy_p = copy_head
        while p:
            copy = RandomListNode(p.label)
            copy.ori = p
            p.copy = copy
            copy_p.next = copy
            copy_p = copy_p.next
            p = p.next
        copy_head = copy_head.next
        copy_p = copy_head
        while copy_p:
            if copy_p.ori.random != None:
                copy_p.random = copy_p.ori.random.copy
            copy_p = copy_p.next

        p = head
        while p:
            del p.copy
            p = p.next

        copy_p = copy_head
        while copy_p:
            del copy_p.ori
            copy_p = copy_p.next

        return copy_head
