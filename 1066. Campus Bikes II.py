import heapq


class Solution:
    def assignBikes(self, workers: list, bikes: list) -> int:
        dis = {}
        N_workers = len(workers)
        M_bikes = len(bikes)
        visited = set()
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dis[i, j] = abs(w[0] - b[0]) + abs(w[1] - b[1])

        heap = []
        cost, wi, bs = [0, 0, 0]
        while wi < N_workers:
            if wi == N_workers:
                return cost
            if (wi, bs) not in visited:
                visited.add((wi, bs))
                for i in range(M_bikes):
                    if (bs >> i) & 1 == 0:
                        # print(i,bs,(bs>>i)&1)
                        heapq.heappush(heap, [cost + dis[wi, i], wi + 1, bs | (1 << i)])
            cost, wi, bs = heapq.heappop(heap)
        return cost


# import heapq
#
#
# class Solution:
#     def assignBikes(self, workers: list, bikes: list) -> int:
#         dis = {}
#         N_workers = len(workers)
#         M_bikes = len(bikes)
#         visited = set()
#         for i, w in enumerate(workers):
#             for j, b in enumerate(bikes):
#                 dis[i, j] = abs(w[0] - b[0]) + abs(w[1] - b[1])
#
#         heap = []
#         cost, wi, bs = [0, 0, tuple(range(M_bikes))]
#         while wi < N_workers:
#             if wi == N_workers:
#                 return cost
#             if (wi, bs) not in visited:
#                 visited.add((wi, bs))
#                 for i, b in enumerate(bs):
#                     # print(i,bs,(bs>>i)&1)
#                     new_bs = tuple(bs[:i] + bs[i + 1:])
#                     heapq.heappush(heap, [cost + dis[wi, b], wi + 1, new_bs])
#             cost, wi, bs = heapq.heappop(heap)
#         return cost


workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]
workers = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
bikes = [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [7, 999], [8, 999]]
workers = [[239, 904], [191, 103], [260, 117], [86, 78], [747, 62]]
bikes = [[660, 8], [431, 772], [78, 576], [894, 481], [451, 730], [155, 28]]
print(Solution().assignBikes(workers, bikes))
