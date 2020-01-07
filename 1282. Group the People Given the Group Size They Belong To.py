import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n=len(groupSizes)
        d={}
        ans=[]
        for i,id_ in enumerate(groupSizes):
            d.setdefault(i,(0,[]))
            d[i][0]+=1
            d[i][1].append(id_)
        for k in d.items():
            groups=d[k][0]//k
            for _ in range(groups):
                temp=d[k][1][:k]
                ans.append(temp)
                d[k][1]=d[k][1][k:]
        return ans








