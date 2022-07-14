from typing import List
import collections


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for xg, yg in guards:
            rows[xg].append((yg, "G"))
            cols[yg].append((xg,"G"))

        for xw, yw in walls:
            rows[xw].append((yw, "W"))
            cols[yw].append((xw,"W"))

        for row in rows.values():
            row.append((-1, "W"))
            row.append((n, "W"))
            row.sort()

        for col in cols.values():
            col.append((-1, "W"))
            col.append((m, "W"))
            col.sort()

        guarded_cells = set()
        for x in rows:
            row = rows[x]
            guarded = []
            left = right = None
            flag = False
            for i in range(len(row)):
                if row[i][1] == "W":
                    if flag:
                        right = row[i][0]
                        guarded.append((left + 1, right - 1))
                    left = row[i][0]
                    flag = False
                elif row[i][1] == "G":
                    flag = True
            # print(x,row,guarded)
            for a, b in guarded:
                for i in range(a, b + 1):
                    guarded_cells.add((x, i))

        for y in cols:
            col = cols[y]
            guarded = []
            left = right = None
            flag = False
            for i in range(len(col)):
                if col[i][1] == "W":
                    if flag:
                        right = col[i][0]
                        guarded.append((left + 1, right - 1))
                    left = col[i][0]
                    flag = False
                elif col[i][1] == "G":
                    flag = True
            # print(y,col,guarded)

            for a, b in guarded:
                for i in range(a, b + 1):
                    guarded_cells.add((i, y))


        return m * n - len(walls) - len(guarded_cells)