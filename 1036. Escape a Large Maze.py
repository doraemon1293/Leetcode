class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        blocked = set([tuple(x) for x in blocked])
        visited = set()
        N = 10 ** 6
        # bfs source
        q = [source]
        while q and len(q) < len(blocked):
            new_q = []
            for x, y in q:
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < N and 0 <= ty < N and (tx, ty) not in visited and (tx, ty) not in blocked:
                        if [tx, ty] == target:
                            return True
                        else:
                            new_q.append((tx, ty))
                            visited.add((tx, ty))
            q = new_q
        print(q)
        if q:
            q = [target]
            while q and len(q) < len(blocked):
                new_q = []
                for x, y in q:
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        tx, ty = x + dx, y + dy
                        if 0 <= tx < N and 0 <= ty < N and (tx, ty) not in visited and (tx, ty) not in blocked:
                            if [tx, ty] == source:
                                return True
                            else:
                                new_q.append((tx, ty))
                                visited.add((tx, ty))
                q = new_q
            if q:
                return True
            else:
                return False
        else:
            return False


blocked = []
source = [0, 0]
target = [999999, 999999]
print(Solution().isEscapePossible(blocked, source, target))
