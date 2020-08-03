class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = [(-(point[0] ** 2 + point[1] ** 2), point) for point in points[:K]]
        heapq.heapify(heap)

        for point in points[K:]:
            heapq.heappushpop(heap, (-(point[0] ** 2 + point[1] ** 2), point))
        return [x[1] for x in heap]
points=[[1,3],[-2,2]]
K=1
print(Solution().kClosest(points,K))