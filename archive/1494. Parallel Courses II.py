from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pre = [0] * n
        dp = {}

        for a, b in dependencies:
            pre[b - 1] |= 1 << (a - 1)  # pre[j]&(1<<i) => course j require course i
        semesters = 0
        status = 0  # status & (1<<i) => course i is finished
        q = [status]

        def comb(items, k):
            for i in range(len(items) - k + 1):
                v = items[i]
                if k == 1:
                    yield 1 << v
                else:
                    rest = items[i + 1:]
                    for c in comb(rest, k - 1):
                        yield (1 << v) + c

        while q:
            new_q = []
            semesters += 1
            for status in q:
                avail = []
                for i in range(n):
                    if status & (1 << i) == 0:
                        if pre[i] & status == pre[i]:
                            avail.append(i)
                for delta_status in comb(avail, min(len(avail), k)):
                    new_status = delta_status | status
                    if new_status == (2 ** n) - 1:
                        return semesters
                    elif new_status not in dp:
                        dp[new_status] = semesters
                        new_q.append(new_status)
            q = new_q
        return -1


n = 4
dependencies = [[2, 1], [3, 1], [1, 4]]
k = 2
print(Solution().minNumberOfSemesters(n, dependencies, k))
