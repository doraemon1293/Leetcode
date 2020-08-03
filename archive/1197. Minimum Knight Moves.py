from collections import deque


class Solution(object):
    def minKnightMoves(self, tx, ty):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if tx == ty == 0:
            return 0
        one_step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
        tx=abs(tx)
        ty=abs(ty)
        q = deque()
        q.append((0, 0, 0))
        visited = {(0, 0)}
        while q:
            x, y, steps = q.popleft()
            for i in range(len(one_step)):
                dx, dy = one_step[i]
                x1, y1 = abs(x + dx), abs(y + dy)
                if (x1, y1) not in visited:
                    visited.add((x1, y1))
                    q.append((x1, y1, steps + 1))
                    if (x1, y1) == (tx, ty):
                        return steps + 1


print(Solution().minKnightMoves(114,
                                -179))
