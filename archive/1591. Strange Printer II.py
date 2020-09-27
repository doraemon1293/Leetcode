from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rec = {}
        colours = set()
        M, N = len(targetGrid), len(targetGrid[0])
        for x in range(M):
            for y in range(N):
                colour = targetGrid[x][y]
                if colour not in colours:
                    rec[colour] = [x, y, x, y]
                    colours.add(colour)
                else:
                    x1, y1, x2, y2 = rec[colour]
                    rec[colour] = [min(x1, x), min(y1, y), max(x2, x), max(y2, y)]

        def foo(colour):
            x1, y1, x2, y2 = rec[colour]
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if targetGrid[x][y] != 0 and targetGrid[x][y] != colour:
                        return False
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    targetGrid[x][y] = 0
            return True

        while colours:
            flag=False
            for colour in colours:
                if foo(colour):
                    colours.remove(colour)
                    flag=True
                    break
            if not flag:
                break
        if colours:
            return False
        else:
            return True

