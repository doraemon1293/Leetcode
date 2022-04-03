class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = d = 0
        visited = set()
        cleaned = set()
        M, N = len(room), len(room[0])
        while (x, y, d) not in visited:
            visited.add((x, y, d))
            cleaned.add((x, y))
            x1, y1 = dxy[d] + x, dxy[d] + y
            if not (0 <= x1 < M and 0 <= y1 < N and room[x1][y1] == 0):
                d = (d + 1) % 4
            else:
                x,y=x1,y1
        return len(cleaned)