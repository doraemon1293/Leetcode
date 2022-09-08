# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root, start: int) -> int:
        def inorder(node,p):
            if node:
                node.p=p
                if node.val==start:
                    self.start=node
                inorder(node.left,node)
                inorder(node.right,node)

        inorder(root,None)
        q=[self.start]
        minutes=0
        infected=set([self.start])
        while q:
            new_q=[]
            for node0 in q:
                for node1 in [node0.p,node0.left,node0.right]:
                    if node1 and node1 not in infected:
                        new_q.append(node1)
                        infected.add(node1)
            q=new_q
            if q==[]:
                return minutes
            minutes+=1

def list_to_tree(arr):
    from collections import deque
    if arr == [] or arr[0] == None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    l_r = "left"
    for x in arr[1:]:
        node = None if x == None else TreeNode(x)
        if l_r == "left":
            q[0].left = node
            if node != None: q.append(node)
            l_r = "right"
        else:
            q[0].right = node
            if node != None: q.append(node)
            q.popleft()
            l_r = "left"
    return root
root = list_to_tree([3,5])
start = 3
print(Solution().amountOfTime(root,start))

