from typing import List
import heapq
import collections


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        indice = collections.defaultdict(collections.deque)
        for i, rain in enumerate(rains):
            indice[rain].append(i)
        for k in indice:
            indice[k].popleft()
        filled_lakes = set()
        heap = []
        ans = []
        for i, rain in enumerate(rains):
            if rain != 0:
                if rain in filled_lakes:
                    return []
                else:
                    if indice[rain]:
                        heapq.heappush(heap, (indice[rain].popleft(), rain))
                    filled_lakes.add(rain)
                ans.append(-1)
            else:
                if heap:
                    ind, lake = heapq.heappop(heap)
                    ans.append(lake)
                    filled_lakes.remove(lake)
                else:
                    ans.append(1)

        return ans