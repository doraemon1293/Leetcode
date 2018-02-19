
# coding=utf-8
'''
Created on 2017å¹?11æœ?12æ—?

@author: Administrator
'''
# from data_structure.Link import list_to_list_node, output
#
#
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        p = root
        n = 0
        while p:
            p = p.next
            n += 1
        shang = n / k
        yu = n % k
        arr = [shang] * k
        for i in xrange(yu):
            arr[i] += 1
        ans = [None] * k
        p = root
        lastP = None
        for ind in xrange(k):
            ans[ind] = p
            while arr[ind]:
                lastP = p
                p = p.next
                arr[ind] -= 1
            if lastP:
                lastP.next = None
        return ans


root = list_to_list_node ([])
k = 3
for x in Solution().splitListToParts(root, k):
    if x:
        print output(x)
    else:
        print x

