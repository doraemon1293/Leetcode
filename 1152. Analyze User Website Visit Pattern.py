import collections, itertools


class Solution:

    def mostVisitedPattern(self, username, timestamp, website):
        visits = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            visits[u].append(w)
        d = collections.defaultdict(int)
        maxi_v = 0
        ans = []
        for user, visit in visits.items():
            for pattern in set(itertools.combinations(visit, 3)):
                d[pattern] += 1
        for k, v in d.items():
            if v > maxi_v:
                maxi_v = v
                ans = [k]
            elif v == maxi_v:
                ans.append(k)
        return sorted(ans)[0]