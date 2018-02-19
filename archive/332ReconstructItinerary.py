# coding=utf-8
'''
Created on 2017å¹?7æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        import bisect
        from_to = defaultdict(list)
        for f, t in sorted(tickets):
            from_to[f].append(t)
        self.route = ["JFK"]
        print from_to

        def dfs(dep):
            if len(self.route) == len(tickets) + 1:
                return True
            for dest in from_to[dep]:
                from_to[dep].remove(dest)
                self.route.append(dest)
                if dfs(dest):
                    return True
                self.route.pop()
                bisect.insort(from_to[dep], dest)
            return False

        dfs("JFK")
        return self.route


tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print Solution().findItinerary(tickets)
