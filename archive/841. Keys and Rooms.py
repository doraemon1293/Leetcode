class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtyp
        """
        N=len(rooms)
        from collections import deque
        q=deque([0])
        opened=set([0])
        while q:
            room=q.popleft()
            for key in rooms[room]:
                if key not in opened:
                    q.append(key)
                    opened.add(key)
                    if len(opened)==N:
                        return True


        return len(opened)==N
rooms=[[1],[2],[3],[]]
print(Solution().canVisitAllRooms(rooms))