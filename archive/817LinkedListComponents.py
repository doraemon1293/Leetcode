# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        from collections import  Counter
        G=Counter(G)
        ans=0
        status=False
        while head and G:
            val=head.val
            if val in G:
                if status==False:
                    status=True
                    ans+=1
                G[val]-=1
                if G[val]==0: del G[val]
            else:
                if status:
                    status=False
            head=head.next
        return ans
G = [0, 3, 1, 4]
print(Solution().numComponents(head,G))


