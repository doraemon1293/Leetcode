# coding=utf-8
'''
Created on 2017å¹?5æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        q = deque()
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(rooms), len(rooms[0]) if rooms else 0
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        def valid(x, y, step):
            return 0 <= x < m and 0 <= y < n and rooms[x][y] != -1  and rooms[x][y] > step

        while q:
            x, y, step = q.popleft()
            for x_d, y_d in delta:
                if valid(x + x_d, y + y_d, step + 1):
                    rooms[x + x_d][y + y_d] = step + 1
                    q.append((x + x_d, y + y_d, step + 1))


rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
Solution().wallsAndGates(rooms)
print rooms
for x in rooms:
    print x

