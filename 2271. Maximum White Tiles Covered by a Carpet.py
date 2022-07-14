from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()

        p1 = p2 = 0
        ans = 0
        covered = 0
        while p2 < len(tiles):
            left = tiles[p1][0]
            right = left + carpetLen - 1
            while p2 < len(tiles) and tiles[p2][1] <= right:
                covered += tiles[p2][1] - tiles[p2][0] + 1
                p2 += 1
            if p2 < len(tiles):
                temp = max(0, right - tiles[p2][0] + 1)
            else:
                temp = 0
            ans = max(ans, covered + temp)
            # print(p1, p2, covered, left, right)
            covered -= tiles[p1][1] - tiles[p1][0] + 1
            p1 += 1
        return ans