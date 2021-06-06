from typing import List
import heapq

import collections


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        avai_server = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(avai_server)
        busy_server = []
        tasks = collections.deque([(i, c) for i, c in enumerate(tasks)])
        cur_sec = 0
        ans = [-1] * len(tasks)
        while tasks:
            if tasks[0][0] > cur_sec:
                cur_sec = tasks[0][0]

            while busy_server and busy_server[0][0] <= cur_sec:
                _, weight, ind = heapq.heappop(busy_server)
                heapq.heappush(avai_server, (weight, ind))
            if avai_server:
                weight, ind_server = heapq.heappop(avai_server)
                ind_task, cost = tasks.popleft()
                ans[ind_task] = ind_server
                heapq.heappush(busy_server, (cur_sec + cost, weight, ind_server))
            else:
                cur_sec = busy_server[0][0]
        return ans


