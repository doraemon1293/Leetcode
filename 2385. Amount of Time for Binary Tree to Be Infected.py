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