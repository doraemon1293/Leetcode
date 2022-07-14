"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        # self.p=None
        # self.q=None
        q_is_subtree_of_p=False

        parent={root:None}

        queue=[root]

        while queue:
            new_queue=[]
            for node in queue:
                for child in node.children:
                    parent[child]=node
                    new_queue.append(child)
            queue=new_queue
        if parent[p]==q:
            return root

        node=q
        while node:
            if node==p:
                q_is_subtree_of_p=True
                break
            node=parent[node]



        if q_is_subtree_of_p:
            if p==root:
                parent[q].children.remove(q)
                q.children.append(p)
                root=q
            else:
                ind_p=parent[p].children.index(p)
                parent[q].children.remove(q)
                q.children.append(p)
                parent[p].children[ind_p]=q

        else:
            parent[p].children.remove(p)
            q.children.append(p)

        return root



