from typing import List
import bisect
import collections


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms = collections.deque(sorted([(y, x) for x, y in rooms], reverse=True))#(size,id)
        ans = [-1] * len(queries)
        avail_rooms = []
        queries = sorted([(y, x, i) for i, (x, y) in enumerate(queries)], reverse=True)#(size,prefer,index)
        # print(rooms)
        # print(queries)
        for minsize, prefered, ind in queries:
            while rooms and rooms[0][0] >= minsize:
                bisect.insort(avail_rooms,rooms.popleft()[1])
            # print("-",avail_rooms)
            if avail_rooms:
                i=bisect.bisect_left(avail_rooms,prefered)
                res=avail_rooms[i] if i <len(avail_rooms) else float("inf")
                if i>0 and abs(avail_rooms[i-1]-prefered)<=abs(res-prefered):
                    res=avail_rooms[i-1]
                ans[ind]=res
            else:
                ans[ind]=-1
        return ans


print(Solution().closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]))