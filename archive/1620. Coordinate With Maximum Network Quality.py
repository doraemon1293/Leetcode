from typing import List
import collections


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        q_dict = collections.defaultdict(int)
        radius2 = radius ** 2
        for tower in towers:
            x, y, q = tower
            # xlim=[max(x-radius,0),min(x+radius+1,50)]
            # ylim = [max(y - radius,0), min(y + radius+1,50)]
            xlim = [max(x - radius, 0), min(x + radius, 50)]
            ylim = [max(y - radius, 0), min(y + radius, 50)]
            for x0 in range(xlim[0], xlim[1] + 1):
                for y0 in range(ylim[0], ylim[1] + 1):
                    d = ((x - x0) ** 2 + (y - y0) ** 2)
                    if d <= radius2:
                        q_dict[x0, y0] += int(q / (1 + d ** 0.5))
        max_v = max(q_dict.values())
        return sorted([k for k, v in q_dict.items() if v == max_v])[0]