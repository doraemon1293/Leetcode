import collections
import heapq


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        heap = []

        tasks = collections.deque(sorted([(s, i, p) for i, (s, p) in enumerate(tasks)]))
        cur_time = 0
        finished_task = []
        while heap or tasks:
            if tasks and cur_time < tasks[0][0] and heap == []:
                cur_time = tasks[0][0]

            while tasks and tasks[0][0] <= cur_time:
                s, i, p = tasks.popleft()
                heapq.heappush(heap, (p, i))
            # print(heap)
            p, i = heapq.heappop(heap)
            cur_time += p
            finished_task.append(i)
        return finished_task