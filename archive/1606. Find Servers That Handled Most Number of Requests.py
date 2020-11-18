import collections
from typing import List
import heapq
import bisect
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        finish_tasks={}
        for i in range(k):
            finish_tasks[i]=0
        avai_server=list(range(k))
        avai_time=[]
        ith=0
        def find_server(ind,avail_server):
            i=bisect.bisect_left(avai_server,ind)
            if i==len(avai_server):
                return avai_server[0]
            else:
                return avai_server[i]

        for arrival_,load_ in zip(arrival,load):
            while avai_time and avai_time[0][0]<=arrival_:
                server=heapq.heappop(avai_time)[1]
                bisect.insort(avai_server,server)
            ind=ith%k
            if avai_server:
                i=find_server(ind,avai_server)
                finish_tasks[i]+=1
                avai_server.remove(i)
                heapq.heappush(avai_time,(arrival_+load_,i))
            ith+=1
        maxi=max(finish_tasks.values())
        # print(finish_tasks)
        return [k for k in finish_tasks if finish_tasks[k]==maxi]