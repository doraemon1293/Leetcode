from typing import List
import collections
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=collections.defaultdict(set)
        for _id,minute in logs:
            d[_id].add(minute)
        c=collections.Counter([len(d[k]) for k in d])
        return [c.get(j,0) for j in range(1,k+1)]
