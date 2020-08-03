from typing import List
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        parents={}
        for i,p in enumerate(parent):
            parents[i]=p
        self.parents=[parents]
        for i in range(15):
            parent={}
            for node,p in self.parents[-1].items():
                if p==-1:
                    parent[node]=-1
                else:
                    parent[node]=self.parents[-1][p]
            self.parents.append(parent)

        for i in range(len(self.parents)):
            print(self.parents[i])


    def getKthAncestor(self, node: int, k: int) -> int:
        kbin=bin(k)[2:][::-1]

        for i in range(len(kbin)):
            if kbin[i]=="1":
                node=self.parents[i][node]
                if node==-1:
                    return -1
        return node



n=7
parent=[-1,0,0,1,1,2,2]
o=TreeAncestor(n,parent)
# print()

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)