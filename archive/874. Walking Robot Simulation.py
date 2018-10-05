class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles = set([tuple(x) for x in obstacles])
        x0, y0 = 0, 0
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direct = 0
        max_dis = 0
        for command in commands:
            if command == -2:
                direct = (direct + 1) % 4
            elif command == -1:
                direct = (direct - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = directions[direct]
                    x1, y1 = x0 + dx, y0 + dy
                    if (x1, y1) in obstacles:
                        break
                    x0, y0 = x1, y1
                    max_dis = max(max_dis, x0 ** 2 + y0 ** 2)
        return max_dis
