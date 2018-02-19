# coding=utf-8
'''
Created on 2017å¹?6æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        import heapq
        m, n = len(maze), len(maze[0])
        visited = set()
        q = []
        hole = tuple(hole)
        heapq.heappush(q, ((0, ""), tuple(ball)))
        self.ans = (float("inf"), "")

        def visit(dis, p, d):
            # 0 up 1 down 2 left 3 right
            dis, path = dis
            i, j = p
            if d == 0:
                s = "u"
            elif d == 1:
                s = "d"
            elif d == 2:
                s = "l"
            elif d == 3:
                s = "r"
            path += s
            if d == 0:
                while i - 1 >= 0 and maze[i - 1][j] != 1:
                    i -= 1
                    dis += 1
                    if (i, j) == hole:
                        # print dis, path
                        if (dis, path) <= self.ans:
                            self.ans = (dis, path)
            if d == 1:
                while i + 1 < m and maze[i + 1][j] != 1:
                    i += 1
                    dis += 1
                    if (i, j) == hole:
                        # print dis, path
                        if (dis, path) <= self.ans:
                            self.ans = (dis, path)

            if d == 2:
                while j - 1 >= 0 and maze[i][j - 1] != 1:
                    j -= 1
                    dis += 1
                    if (i, j) == hole:
                        # print dis, path
                        if (dis, path) <= self.ans:
                            self.ans = (dis, path)
            if d == 3:
                while j + 1 < n and maze[i][j + 1] != 1:
                    j += 1
                    dis += 1
                    if (i, j) == hole:
                        # print dis, path
                        if (dis, path) <= self.ans:
                            self.ans = (dis, path)
            if (i, j) not in visited:
                heapq.heappush(q, ((dis, path), (i, j)))

        while q:
            dis, p = heapq.heappop(q)
            # print dis, p
            if dis[0] > self.ans[0]:
                break
            visited.add(p)
            for d in xrange(4):
                visit(dis, p, d)
        # print self.ans
        if self.ans[0] != float("inf"):
            return self.ans[1]
        else:
            return "impossible"


maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [0, 1]
print Solution().findShortestWay(maze, ball, hole)
