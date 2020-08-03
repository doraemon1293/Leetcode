class Solution:
    def shortestDistanceColor(self, colors: list, queries: list) -> list:
        closest = [[float("inf")] * 4 for _ in range(len(colors))]
        cur_closest = [-float("inf")] * 4
        for i in range(len(colors)):
            c = colors[i]
            cur_closest[c] = i
            closest[i] = [min(i - cur_closest[c], closest[i][c]) for c in (0,1, 2, 3)]
        cur_closest = [float("inf")] * 4
        for i in range(len(colors) - 1, -1, -1):
            c = colors[i]
            cur_closest[c] = i
            closest[i] = [min(cur_closest[c] - i, closest[i][c]) for c in (0,1, 2, 3)]

        ans = [-1 if closest[i][c] == float("inf") else closest[i][c] for i, c in queries]
        return ans


colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
queries = [[1, 3], [2, 2], [6, 1]]
print(Solution().shortestDistanceColor(colors, queries))
