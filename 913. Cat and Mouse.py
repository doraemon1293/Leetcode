from collections import deque, defaultdict


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # state (mouse's position, cat's position, turn(True mouse False Cat), (win status draw 0 mouse win 1 cat win 2)

        def get_parents(state):
            m, c, t = state
            # cat's turn, so last turn is mouse
            res = []
            if t:
                for node in graph[c]:
                    if node != 0:
                        res.append((m, node, not t))
            else:
                for node in graph[m]:
                    res.append((node, c, not t))
            return res

        N = len(graph)
        degree = {}
        q = deque()
        colors = defaultdict(int)
        for m in range(N):
            for c in range(N):
                degree[m, c, True] = len(graph[m])
                degree[m, c, False] = len(graph[c]) - (0 in graph[c])

        for i in range(1, N):
            colors[i, i, True] = 2
            state = (i, i, True, 2)
            q.append(state)
            colors[i, i, False] = 2
            state = (i, i, False, 2)
            q.append(state)

        for i in range(N):
            colors[0, i, True] = 1
            state = (0, i, True, 1)
            q.append(state)
            colors[0, i, False] = 1
            state = (0, i, False, 1)
            q.append(state)
        while q:
            m, c, t, color = q.popleft()
            # t==true => mouse turn =>last turn is cat
            for m1, c1, t1 in get_parents((m, c, t)):
                if colors[m1, c1, t1] == 0:
                    # parent node is mouse's turn and child node mouse win or cat's turn and cat win
                    if (t1 and color == 1) or ((not t1) and color == 2):
                        colors[m1, c1, t1] = color
                        q.append((m1, c1, t1, colors[m1, c1, t1]))
                    else:
                        degree[m1, c1, t1] -= 1
                        if degree[m1, c1, t1] == 0:
                            colors[m1, c1, t1] = color
                            q.append((m1, c1, t1, colors[m1, c1, t1]))

        return colors[1, 2, True]


graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
graph = [[6], [4], [9], [5], [1, 5], [3, 4, 6], [0, 5, 10], [8, 9, 10], [7], [2, 7], [6, 7]]
print(Solution().catMouseGame(graph))
