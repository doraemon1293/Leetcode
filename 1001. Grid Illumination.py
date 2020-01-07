from collections import defaultdict


class Solution:
    def gridIllumination(self, N: int, lamps, queries):
        ans = []
        row = defaultdict(set)
        col = defaultdict(set)
        # diagonal from left-bottom to right-top denoted by x+y (x+y) euuals=>in the same dignonal
        diag_plus = defaultdict(set)
        # diagonal from left-top to right-bottom denoted by x-y (x-y) euuals=>in the same dignonal
        diag_minus = defaultdict(set)
        adjacent = defaultdict(set)
        removed_lamp=set()
        for x, y in lamps:
            row[x].add((x, y))
            col[y].add((x, y))
            diag_plus[x + y].add((x, y))
            diag_minus[x - y].add((x, y))
            adjacent[x, y].add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1,-1),(1,-1),(-1,1)):
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    adjacent[x + dx, y + dy].add((x, y))
        for x, y in queries:
            if len(row[x]) > 0 or len(col[y]) > 0 or len(diag_minus[x - y]) > 0 or len(diag_plus[x + y]) > 0:
                ans.append(1)
            else:
                ans.append(0)
            for x_lamp, y_lamp in adjacent[x, y]:
                row[x_lamp].discard((x_lamp, y_lamp))
                col[y_lamp].discard((x_lamp, y_lamp))
                diag_plus[x_lamp + y_lamp].discard((x_lamp, y_lamp))
                diag_minus[x_lamp - y_lamp].discard((x_lamp, y_lamp))
        return ans

N=5
lamps=[[0,0],[4,4]]
queries=[[1,1],[1,0]]
print(Solution().gridIllumination(N,lamps,queries))