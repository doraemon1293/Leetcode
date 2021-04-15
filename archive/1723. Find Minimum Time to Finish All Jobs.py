from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        job_n = len(jobs)
        jobs.sort(reverse=True)
        workloads = [0] * k
        for i in range(job_n):
            workloads[i % k] += jobs[i]
        self.ans = max(workloads)

        workloads = [0] * k

        def dfs(i, cur_max):
            if i == job_n:
                self.ans = min(self.ans, cur_max)
                return
            searched_workload=set()
            for j in range(k):
                if workloads[j] not in searched_workload:
                    if workloads[j] + jobs[i] < self.ans:
                        searched_workload.add(workloads[j])
                        workloads[j] += jobs[i]
                        dfs(i + 1, max(cur_max, workloads[j]))
                        workloads[j] -= jobs[i]

        dfs(0, 0)

        return self.ans