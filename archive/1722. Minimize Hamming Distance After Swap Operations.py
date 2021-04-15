from typing import List
import collections
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf={}
        for i in range(len(source)):
            uf[i]=i
        def find(x):
            root=x
            path=[]
            while uf[root]!=root:
                root=uf[root]
                path.append(root)
            for node in path:
                uf[node]=root
            return root

        def connect(x,y):
            uf[find(x)]=uf[find(y)]

        for x,y in allowedSwaps:
            connect(x,y)
        # print(uf)
        #
        # for i in range(len(source)):
        #     print(i,find(i))



        lists1={}
        lists2={}
        for i in range(len(source)):
            root=find(i)
            lists1.setdefault(root,[])
            lists2.setdefault(root,[])
            lists1[root].append(source[i])
            lists2[root].append(target[i])
        ans=0
        for root in lists1:
            c1=collections.Counter(lists1[root])
            c2=collections.Counter(lists2[root])
            # print(root)
            # print(c1)
            # print(c2)
            # print(sorted(lists1[root]))
            # print(sorted(lists2[root]))
            for k in c1:
                ans+=max(c1[k]-c2.get(k,0),0)

        return ans