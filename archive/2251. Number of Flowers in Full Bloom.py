import bisect
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        arr={}
        for a,b in flowers:
            arr.setdefault(a,0)
            arr[a]+=1
            arr.setdefault(b+1,0)
            arr[b+1]-=1
        arr=sorted([(t,delta) for t,delta in arr.items()])

        bloom=[(0,0)]
        for i in range(len(arr)):
            t,delta=arr[i]
            cur=bloom[-1][1]
            bloom.append((t,cur+delta))
        ans=[]
        for t in persons:
            ind=bisect.bisect_left(bloom,(t,float("inf")))-1
            ans.append(bloom[ind][1])
        return ans






