from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        nodes=[[-1,-1] for i in range(len(parents))]
        for i,p in enumerate(parents):
            if p==-1:
                root=i
            else:
                if nodes[p][0]==-1:
                    nodes[p][0]=i
                else:
                    nodes[p][1] = i

        size={}
        def postorder(node):
            if node!=-1:
                left_size=postorder(nodes[node][0])
                right_size=postorder(nodes[node][1])
                size[node]=left_size+right_size+1
                return size[node]
            else:
                return 0
        postorder(root)
        # print(size)
        # print(nodes)
        highest_score=-1
        ans=[]

        for i in range(len(nodes)):
            left,right=nodes[i]
            parent=parents[i]
            left_size=size[left] if left!=-1 else 0
            right_size=size[right] if right!=-1 else 0
            if parent == -1:
                parent_size=0
            else:
                parent_size=size[root]-size[i]
            arr=[x for x in [left_size,right_size,parent_size] if x!=0]
            if len(arr):
                score=1
                for x in arr:
                    score*=x
            else:
                score=0
            # print(i,left,right,parent,left_size,right_size,parent_size,score)
            if score==highest_score:
                ans.append(i)
            elif score>highest_score:
                highest_score=score
                ans=[i]
        return len(ans)